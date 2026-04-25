#!/usr/bin/env python3
"""
experiment/main.py — canonical entry point for the SLE 2026 artifact.

Usage:
    python experiment/main.py --language lua
    python experiment/main.py --language ALL
    python experiment/main.py --config configurations/sle_paper.json --language ocl

RunAnalysis.local_dir_path() returns os.path.dirname(os.getcwd()).  We must
therefore run from inside a first-level subdirectory of the project root.
This script achieves that by calling os.chdir() to its own directory
(experiment/) at start-up, so local_dir_path() resolves to the project root.
"""

import argparse
import importlib.util
import json
import os
import sys
import subprocess

# ---------------------------------------------------------------------------
# Path bootstrap — must happen before any project import
# ---------------------------------------------------------------------------

_EXPERIMENT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_EXPERIMENT_DIR)

# Ensure local_dir_path() in RunAnalysis resolves correctly.
os.chdir(_EXPERIMENT_DIR)

# Make core/, languages/, generation/, run/ importable.
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

# ---------------------------------------------------------------------------
# Project imports (after sys.path is set)
# ---------------------------------------------------------------------------

from core.generate_keyword_features import KeywordGroupingGenerator
from core.jupyter_writer import KeywordResultWriter

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_LOADED_MODULES: dict = {}


def _load_run_module(language: str):
    """Dynamically load /run/<language>.py without requiring __init__.py."""
    if language in _LOADED_MODULES:
        return _LOADED_MODULES[language]

    run_file = os.path.join(_PROJECT_ROOT, "run", f"{language}.py")
    if not os.path.isfile(run_file):
        raise FileNotFoundError(f"Run script not found: {run_file}")

    module_name = f"_run_{language}"
    spec = importlib.util.spec_from_file_location(module_name, run_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    _LOADED_MODULES[language] = module
    return module


def _run_dataset(module, ds_entry: dict, language: str) -> object:
    """Instantiate the run class, set extra attributes, and call run_analysis()."""
    class_name = ds_entry["run_class"]
    ds_name = ds_entry["name"]

    run_class = getattr(module, class_name)
    instance = run_class()

    # Inject any extra instance attributes declared in the config (e.g. folder).
    for attr in ("folder",):
        if attr in ds_entry:
            setattr(instance, attr, ds_entry[attr])

    print(f"  [{language}] {class_name}.run_analysis({ds_name!r})")
    instance.run_analysis(ds_name)
    return instance


def _write_results(language: str, lang_cfg: dict, last_instance) -> None:
    """Configure and call KeywordResultWriter for a language."""
    rw_cfg = lang_cfg.get("result_writer", {})
    kw_cfg = lang_cfg.get("keywords", {})

    kwgenerator = KeywordGroupingGenerator(
        language=language,
        keywords=last_instance.keywords,
    )

    result = KeywordResultWriter()

    if kw_cfg.get("source") == "semantic_groups_json":
        result.excluded_keywords = kwgenerator.get_excluded_keywords()
        result.grouped_keywords = kwgenerator.get_semantic_groups()

    result.datasets = rw_cfg.get("datasets", [])
    result.ds_groups = rw_cfg.get("ds_groups") or None

    print(f"  [{language}] Writing analysis notebook ...")
    result.write_result_to_file(language)


# ---------------------------------------------------------------------------
# Core orchestration
# ---------------------------------------------------------------------------

def run_language(language: str, lang_cfg: dict) -> None:
    print(f"\n{'=' * 60}")
    print(f"  Language: {language.upper()}")
    print(f"{'=' * 60}")

    module = _load_run_module(language)

    datasets = lang_cfg.get("datasets", [])
    if not datasets:
        print(f"  [{language}] No datasets configured — skipping.")
        return

    last_instance = None
    for ds_entry in datasets:
        last_instance = _run_dataset(module, ds_entry, language)

    _write_results(language, lang_cfg, last_instance)
    print(f"  [{language}] Done.")


def execute_notebook(language: str) -> None:
    notebook = os.path.join(_PROJECT_ROOT, "analysis", f"{language}.ipynb")
    if not os.path.isfile(notebook):
        print(f"  [{language}] Notebook not found: {notebook} — skipping.")
        return
    print(f"  [{language}] Executing notebook: {notebook}")
    result = subprocess.run(
        [
            sys.executable, "-m", "nbconvert",
            "--to", "notebook",
            "--execute", notebook,
            "--inplace",
        ],
        check=False,
    )
    if result.returncode != 0:
        print(f"  [{language}] WARNING: nbconvert exited with code {result.returncode}.")

def execute_all_together_notebook() -> None:
    notebook = os.path.join(_PROJECT_ROOT, "analysis", "_all_together.ipynb")
    if not os.path.isfile(notebook):
        print(f"all_together.ipynb Notebook not found: {notebook} — skipping.")
        return
    print(f"Executing notebook: {notebook}")
    result = subprocess.run(
        [
            sys.executable, "-m", "nbconvert",
            "--to", "notebook",
            "--execute", notebook,
            "--inplace",
        ],
        check=False,
    )
    if result.returncode != 0:
        print(f"WARNING: nbconvert exited with code {result.returncode}")        


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run keyword-coverage analysis for one or all languages.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python experiment/main.py --language lua\n"
            "  python experiment/main.py --language ALL\n"
            "  python experiment/main.py --config configurations/sle_paper.json --language sql\n"
        ),
    )
    parser.add_argument(
        "--config",
        default=os.path.join(_PROJECT_ROOT, "configurations", "sle_paper.json"),
        help="Path to the JSON experiment configuration (default: configurations/sle_paper.json).",
    )
    parser.add_argument(
        "--language",
        metavar="LANG",
        help="Language to run: lua | ocl | plantuml | python3 | r | sql | ALL",
    )
    parser.add_argument(
        "--notebook-only",
        action="store_true",
        help="Skip analysis and only execute the notebook(s) for the specified language(s).",
    )
    parser.add_argument(
        "--all-together-notebook",
        action="store_true",
        help="Skip analysis and only execute the _all_together.ipynb analysis notebook.",
    )

    args = parser.parse_args()

    if not args.all_together_notebook and not args.language:
        parser.error("--language is required unless --all-together-notebook is used.")

    if args.notebook_only and args.all_together_notebook:
        parser.error("--notebook-only and --all-together-notebook are mutually exclusive.")

    config_path = os.path.abspath(args.config)
    if not os.path.isfile(config_path):
        print(f"ERROR: config file not found: {config_path}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as fh:
        config = json.load(fh)

    languages_cfg: dict = config["languages"]
    supported = list(languages_cfg.keys())

    targets = []
    if args.language:
        if args.language.upper() == "ALL":
            targets = supported
        else:
            lang = args.language.lower()
            if lang not in languages_cfg:
                print(
                    f"ERROR: language '{lang}' not found in config.\n"
                    f"Supported: {supported}"
                )
                sys.exit(1)
            targets = [lang]

    for lang in targets:
        if not args.notebook_only and not args.all_together_notebook:
            run_language(lang, languages_cfg[lang])

    if not args.notebook_only and not args.all_together_notebook:
        print("")
        print("="*60)
        print("Everything went perfectly!")
        print("Now, let's execute the generated notebooks...")
        print("="*60)

    if not args.all_together_notebook:
        for lang in targets:
            execute_notebook(lang)

    if len(targets)>1 or args.all_together_notebook:
        print("="*60)
        print("Now, let's execute the notebook that sum up all the results and generates the MAIN result table...")
        print("="*60)
        execute_all_together_notebook()
    

    print("\nAll done.")


if __name__ == "__main__":
    main()