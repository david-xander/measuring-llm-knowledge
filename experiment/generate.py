#!/usr/bin/env python3
"""
experiment/generate.py — entry point for LLM code generation for each language.

Lua and R are skipped — generation was already performed for both HumanEval and MBPP.

Requires OPENAI_API_KEY as an environment variable for OpenAI/Azure-backed models.

Usage:
    python experiment/generate.py --language ocl
    python experiment/generate.py --language ALL
    python experiment/generate.py --language python3 --models gpt-4o-mini gpt-4o
"""

import argparse
import importlib.util
import os
import sys

import pandas as pd

# ---------------------------------------------------------------------------
# Path bootstrap — must happen before any project import
# ---------------------------------------------------------------------------

_EXPERIMENT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT   = os.path.dirname(_EXPERIMENT_DIR)
_GENERATION_DIR = os.path.join(_PROJECT_ROOT, "generation")

# The generation scripts resolve datasets as  ../datasets/  relative to cwd.
# They were designed to be run from inside  generation/ .
os.chdir(_GENERATION_DIR)

if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SUPPORTED_LANGUAGES = ["ocl", "plantuml", "python3", "sql"]
SKIPPED_LANGUAGES   = ["lua", "r"]

ALL_MODELS = [
    "gpt-4o-mini",
    "gpt-4o",
    "DeepSeek-V3.1",
    "Llama-3.3-70B-Instruct",
    "deepseek-coder:6.7b",
    "llama3.1:latest",
]

# ---------------------------------------------------------------------------
# Module loader
# ---------------------------------------------------------------------------

_LOADED_MODULES: dict = {}


def _load_gen_module(script_name: str):
    """Dynamically load a script from generation/ without side-effects."""
    if script_name in _LOADED_MODULES:
        return _LOADED_MODULES[script_name]
    path = os.path.join(_GENERATION_DIR, f"{script_name}.py")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Generation script not found: {path}")
    spec   = importlib.util.spec_from_file_location(f"_gen_{script_name}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"_gen_{script_name}"] = module
    spec.loader.exec_module(module)
    _LOADED_MODULES[script_name] = module
    return module


# ---------------------------------------------------------------------------
# Per-language runners
# ---------------------------------------------------------------------------

def run_ocl(models: list) -> None:
    module       = _load_gen_module("ocl")
    results_path = os.path.join(_GENERATION_DIR, "results", "OCL_ds_generated")
    os.makedirs(results_path, exist_ok=True)
    gen = module.OCLCodeGeneration(language="OCL", models=models, target_path=results_path)
    gen.run()


def run_plantuml(models: list) -> None:
    module       = _load_gen_module("plantuml_modelset")
    results_path = os.path.join(_GENERATION_DIR, "results", "PlantUML_GoldenUMLmodelset_gentest")
    dataset_path = os.path.join(_PROJECT_ROOT, "datasets", "GoldenUMLmodelset")

    ds_list = module.GoldemUMLMOdelsetSpecs(dataset_path)
    df      = pd.DataFrame(ds_list)

    for model in models:
        model_dir = os.path.join(results_path, model.replace("/", ""))
        os.makedirs(model_dir, exist_ok=True)
        gen = module.Task2CodeGeneration(
            testing_ds  = df,
            language    = "PlantUML",
            model       = model,
            target_path = os.path.join(model_dir, "PlantUML_0.csv"),
        )
        gen.run()


def run_python3(models: list) -> None:
    # HumanEval
    heval_mod        = _load_gen_module("python_heval")
    results_heval    = os.path.join(_GENERATION_DIR, "results", "python_humanEval")
    os.makedirs(results_heval, exist_ok=True)
    heval_mod.HumanEvalCodeGeneration(language="Python", models=models, target_path=results_heval).run()

    # MBPP
    mbpp_mod         = _load_gen_module("python_mbpp")
    results_mbpp     = os.path.join(_GENERATION_DIR, "results", "python_mbpp")
    os.makedirs(results_mbpp, exist_ok=True)
    mbpp_mod.MBPPCodeGeneration(language="Python", models=models, target_path=results_mbpp).run()


def run_sql(models: list) -> None:
    module       = _load_gen_module("sql_generation_spider")
    results_path = os.path.join(_GENERATION_DIR, "results", "sql_spider_generated")
    os.makedirs(results_path, exist_ok=True)
    gen = module.SpiderSQLCodeGeneration(models=models, target_path=results_path)
    gen.run()


_RUNNERS = {
    "ocl":      run_ocl,
    "plantuml": run_plantuml,
    "python3":  run_python3,
    "sql":      run_sql,
}

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run LLM code generation for one or all languages.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python experiment/generate.py --language ocl\n"
            "  python experiment/generate.py --language ALL\n"
            "  python experiment/generate.py --language python3 --models gpt-4o-mini gpt-4o\n\n"
            "Note: lua and r are skipped — generation was already performed.\n"
            "Set OPENAI_API_KEY before running OpenAI / Azure-backed models.\n"
        ),
    )
    parser.add_argument(
        "--language",
        metavar="LANG",
        required=True,
        help=(
            "Language to generate for: "
            + " | ".join(SUPPORTED_LANGUAGES)
            + " | ALL  (lua and r are skipped)"
        ),
    )
    parser.add_argument(
        "--models",
        metavar="MODEL",
        nargs="+",
        default=ALL_MODELS,
        choices=ALL_MODELS,
        help=(
            "One or more models to use. "
            "Defaults to all supported models."
        ),
    )

    args = parser.parse_args()

    lang = args.language.lower()

    if lang == "all":
        targets = SUPPORTED_LANGUAGES
    elif lang in SKIPPED_LANGUAGES:
        print(
            f"Language '{lang}' is skipped — generation was already "
            "performed for both HumanEval and MBPP."
        )
        sys.exit(0)
    elif lang not in SUPPORTED_LANGUAGES:
        print(
            f"ERROR: language '{args.language}' not supported.\n"
            f"Supported : {SUPPORTED_LANGUAGES}\n"
            f"Skipped   : {SKIPPED_LANGUAGES}"
        )
        sys.exit(1)
    else:
        targets = [lang]

    print(f"Models : {args.models}")

    for lang in targets:
        print(f"\n{'=' * 60}")
        print(f"  Language: {lang.upper()}")
        print(f"{'=' * 60}")
        _RUNNERS[lang](args.models)
        print(f"  [{lang}] Done.")

    print("\nAll done.")


if __name__ == "__main__":
    main()