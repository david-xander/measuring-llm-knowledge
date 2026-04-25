# How much does an LLM know about my programming language?

This repository is the official artifact for the SLE 2026 paper
**"How much does an LLM know about my programming language?"**.

The framework systematically evaluates LLM proficiency in a programming language
using **ANTLR-based syntactic analysis**: it extracts keywords and grammar rules
from LLM-generated code and measures how much of the language's vocabulary and
structure a model actually uses — even in code that fails to compile.

**Key features:**

- **Granular metrics:** Measures Keyword/Rule Coverage and Production Validity.
- **Partial knowledge capture:** Analyzes syntactically invalid code to identify where a model's knowledge fails.
- **Extensible:** Designed to work with any language that has an ANTLR grammar. → [Adding a New Language](#adding-a-new-language)
- **Automatic reporting:** Generates a complete language coverage report as a Jupyter Notebook.

---

## Supported Languages

The following six languages are fully supported out of the box:

| Language | Grammar style |
|---|---|
| **OCL** | Single combined grammar (`OCL.g4`) |
| **PlantUML** | Split lexer + parser (`PlantUMLLexer.g4` + `PlantUML.g4`) |
| **Python 3** | Split lexer + parser (`Python3Lexer.g4` + `Python3Parser.g4`) |
| **R** | Single grammar with filter (`R.g4` + `RFilter.g4`) |
| **Lua** | Split lexer + parser (`LuaLexer.g4` + `LuaParser.g4`) |
| **SQL** | Split lexer + parser (`MariaDBLexer.g4` + `MariaDBParser.g4`) |

> Want to add a new language or new LLM models? See [Adding a New Language](#adding-a-new-language) and [Extending the Framework](#extending-the-framework).

---

## Artifact Structure

```
measuring-llm-knowledge/
├── experiment/
│   ├── main.py          — analysis entry point (produces results + notebooks)
│   └── generate.py      — LLM code generation entry point (requires API keys)
├── configurations/
│   └── sle_paper.json   — experiment configuration
├── run/                 — per-language analysis runners
├── core/                — shared analysis library
├── languages/           — ANTLR grammars + per-language analyzers + visitors and evaluation
├── datasets/            — input datasets (including LLM-generated code and pre-cached HuggingFace data)
├── results/             — output CSVs written at runtime
├── analysis/            — output Jupyter notebooks written at runtime
├── generation/          — LLM generation scripts
├── Dockerfile
├── docker-build.sh
├── docker-run.sh        — full run (all languages)
└── docker-run-reduced.sh — kick-the-tires run (OCL only)
```

---

## Reproducing the Paper Results (Docker — Recommended)

Docker is the recommended path for artifact evaluation. It requires no local
Python setup and no internet access during the run.

### System Requirements

- Docker Desktop ≥ 24.0 ([download](https://www.docker.com/products/docker-desktop/))
- ~8 GB free disk space (image + outputs)
- ~4 GB RAM

### Step 1 — Build the image

```bash
bash docker-build.sh
```

This builds the `sle2026-artifact` image locally. All dependencies and
datasets are bundled inside; no network access is needed at run time.

### Step 2 — Kick-the-tires (OCL only)

```bash
bash docker-run-reduced.sh
```

Runs the full pipeline for OCL only: analysis → notebook generation → notebook
execution. Confirms the artifact works end-to-end before committing to the full run.
Outputs appear in `analysis/` and `results/` on your host.

### Step 3 — Full run (all languages)

```bash
bash docker-run.sh
```

Runs the full pipeline for all six languages, executes every per-language
notebook, and then executes `analysis/_all_together.ipynb` which produces the
paper's main tables (RQ1 and RQ3).

> **Note:** `_all_together.ipynb` requires results from **all six languages**.
> It is executed automatically only when running `--language ALL`.

Both scripts mount two host directories so outputs are accessible after the run:

| Host path | Contents |
|---|---|
| `./results/` | Raw feature CSVs per language and dataset |
| `./analysis/` | Executed Jupyter notebooks + paper figures (`.pdf`) + paper tables (`.json`) |

---

## Paper Outputs

The following files in `analysis/` correspond directly to paper figures and
tables, generated when the full run completes:

| File | Content | Paper location |
|---|---|---|
| `analysis/4_usage_ocl.pdf` | Keyword usage heatmap — OCL | Figure 2 |
| `analysis/4_usage_python.pdf` | Keyword usage heatmap — Python 3 | Figure 3 |
| `analysis/rq1_table.json` | Coverage and correctness metrics — all languages, LLM-generated datasets | Table 2 |
| `analysis/rq3_table.json` | Coverage and correctness metrics — baseline (non-generated) datasets | Table 3 |

All other figures (coverage bar charts, frequency heatmaps, variance plots,
rule-usage heatmaps) are rendered inline inside the per-language notebooks
(`analysis/ocl.ipynb`, `analysis/python3.ipynb`, etc.).

---

## Running Without Docker

Use this path to run individual languages, inspect intermediate results, or
re-run only the notebooks after a previous analysis.

> This path also allows you to extend the framework with new languages or
> models. → [Extending the Framework](#extending-the-framework)

### Installation

```bash
pip install -r requirements-docker.txt
```

### API Keys

`experiment/main.py` (analysis) requires **no API keys** — it only reads
pre-included datasets.

`experiment/generate.py` (LLM code generation) requires API keys for
cloud-backed models. Set them as environment variables before running:

```bash
# Required for gpt-4o-mini and gpt-4o
export OPENAI_API_KEY='your-openai-key-here'

# Required for DeepSeek-V3.1 and Llama-3.3-70B-Instruct (Azure AI)
export AZUREAI_ENDPOINT_URL='your-azure-endpoint-here'
export AZUREAI_API_KEY='your-azure-key-here'
```

Local models (`deepseek-coder:6.7b`, `llama3.1:latest`) are served via
[Ollama](http://ollama.:11434) and require no API key. If you need to adapt to your use case, you just have to edit the /core/llm_prompting.py file.

---

## `experiment/main.py` — Analysis Entry Point

Runs keyword and syntactic analysis for one or all languages, writes results
to `results/`, generates analysis notebooks in `analysis/`, and executes them.

```
python experiment/main.py [options]
```

| Argument | Description | Default |
|---|---|---|
| `--language LANG` | Language to run: `lua` \| `ocl` \| `plantuml` \| `python3` \| `r` \| `sql` \| `ALL` | *(required unless `--all-together-notebook`)* |
| `--config PATH` | Path to the JSON experiment configuration | `configurations/sle_paper.json` |
| `--notebook-only` | Skip analysis; only execute the notebook(s) for the specified language(s) | off |
| `--all-together-notebook` | Skip language analysis; only execute `analysis/_all_together.ipynb` | off |

**Examples:**

```bash
# Run analysis for OCL and execute its notebook
python experiment/main.py --language ocl

# Run all languages, then execute all notebooks including _all_together.ipynb
python experiment/main.py --language ALL

# Only re-execute a previously generated notebook
python experiment/main.py --language python3 --notebook-only

# Only re-execute the combined results notebook (requires all language results to exist)
python experiment/main.py --all-together-notebook
```

> Must be run from the **project root** (e.g. `python experiment/main.py`).

---

## `experiment/generate.py` — LLM Code Generation Entry Point

Generates LLM code completions for any of the six supported languages and
saves them to `generation/results/`. Results must be **manually copied** to
the appropriate `datasets/` subfolder before running `main.py`.[^1]

> To add support for additional LLM models, see [Extending the Framework](#extending-the-framework).

```
python experiment/generate.py [options]
```

| Argument | Description | Default |
|---|---|---|
| `--language LANG` | Language to generate for: `ocl` \| `plantuml` \| `python3` \| `sql` \| `lua` \| `r` \| `ALL` | *(required)* |
| `--models MODEL [MODEL ...]` | One or more models to use (space-separated) | All six models |

**Supported models:**

| Model | Provider |
|---|---|
| `gpt-4o-mini` | OpenAI (requires `OPENAI_API_KEY`) |
| `gpt-4o` | OpenAI (requires `OPENAI_API_KEY`) |
| `DeepSeek-V3.1` | Azure AI (requires `AZUREAI_API_KEY`) |
| `Llama-3.3-70B-Instruct` | Azure AI (requires `AZUREAI_API_KEY`) |
| `deepseek-coder:6.7b` | Ollama (local, no key required) |
| `llama3.1:latest` | Ollama (local, no key required) |

**Examples:**

```bash
# Generate OCL code with all models
python experiment/generate.py --language ocl

# Generate SQL code with two specific models
python experiment/generate.py --language sql --models gpt-4o-mini gpt-4o

# Generate for all languages
python experiment/generate.py --language ALL
```

**Generation output paths and their `datasets/` targets:**[^1]

| Language | Generated to (`generation/results/`) | Copy to (`datasets/`) |
|---|---|---|
| OCL | `OCL_ds_generated/` | `OCL_ds_generated/` |
| PlantUML | `PlantUML_GoldenUMLmodelset_gentest/<model>/` | `PlantUML_GoldenUMLmodelset_gentest/<model>/` |
| Python 3 | `python_humanEval/` and `python_mbpp/` | `python_humanEval/` and `python_mbpp/` |
| SQL | `sql_spider_generated/` | `sql_spider_generated/` |
| Lua | `lua_multipl-e_generated/humanEval/` and `lua_multipl-e_generated/mbpp/` | `lua_multipl-e_generated/humanEval/` and `lua_multipl-e_generated/mbpp/` |
| R | `r_multipl-e_generated/humanEval/` and `r_multipl-e_generated/mbpp/` | `r_multipl-e_generated/humanEval/` and `r_multipl-e_generated/mbpp/` |

[^1]: After generation, file names must be **manually renamed** to match the
unified naming convention used across the project (e.g.
`DeepSeek-V3.1_spider.csv` → `deepseek.csv`). This convention unifies model
and dataset identifiers across all languages and is required for `main.py` to
locate the files correctly.

---

## Adding a New Language

The framework is designed to work with any language that can be described by
an ANTLR grammar. The supported languages cover a range of grammar styles —
you can use any of them as a starting point:

| Grammar style | Example in this project |
|---|---|
| Single combined grammar | OCL (`languages/ocl/parser/OCL.g4`) |
| Split lexer + parser | Lua (`LuaLexer.g4` + `LuaParser.g4`), SQL (`MariaDBLexer.g4` + `MariaDBParser.g4`), PlantUML (`PlantUMLLexer.g4` + `PlantUML.g4`), Python 3 (`Python3Lexer.g4` + `Python3Parser.g4`) |
| Grammar with auxiliary filter | R (`R.g4` + `RFilter.g4`) |
| External ANTLR meta-grammar | ANTLR itself (`languages/antlr/parser/ANTLRv4Lexer.g4` + `ANTLRv4Parser.g4`) |

Steps to add a new language:

1. **Grammar:** Place your `.g4` file(s) and the ANTLR-generated Python
   artifacts (`.py`, `.interp`, `.tokens`) under `languages/<your_lang>/parser/`.
   Thousands of ready-to-use grammars are available at the
   [ANTLR Grammars repository](https://github.com/antlr/grammars-v4).
2. **Analyzer:** Create `languages/<your_lang>/analyzer.py` and `lib.py`
   based on an existing language (e.g. `languages/ocl/`). Adapt the root
   rule name and any language-specific parametrization (e.g., initial rule of the grammar). Additionally, you need to adapt the visitors (KeywordFrequencyVisitor.py, SequenceVisitor.py and SyntacticAnalisisVisitor.py) according to your language lexer and parser names.
4. **Scope:** This step may be performed automatically by gpt-4o-mini, which requires OpenAI API key defined, as mentioned earlier. However, you can manually define `excluded_keywords` and `grouped_keywords`
   inline in your run script, or in JSON files under
   `languages/<your_lang>/keywords/`, to narrow the analysis to a relevant
   subset of the grammar.
3. **Run script:** Create `run/<your_lang>.py` extending `RunAnalysis`. Point
   it to your dataset and implement `extract_data_from_grammar()` and
   `run_analysis()`. If you can execute this step, you already have everything you need to complete your language analysis. The following step is there to complete the /experiment/main.py script with your language setup.
5. **Configuration (optional):** Add a new entry to `configurations/sle_paper.json` following the schema of the existing languages.

---

## Extending the Framework

The framework is intentionally open-ended. Without major modifications, you can:

**Add new LLM models** — edit `core/llm_factory.py` to route your model name
to the appropriate provider, and add a provider class in
`core/llm_prompting.py` if needed. OpenAI-compatible APIs (including local
servers such as LM Studio) can be added by subclassing `LLMPrompting`. Then
pass the new model name via `experiment/generate.py --models <your_model>`.

**Add new languages** — follow the steps in
[Adding a New Language](#adding-a-new-language). Any language with an ANTLR
grammar can be integrated.

**Add new datasets** — add an entry to `configurations/sle_paper.json` and
place the data file in `datasets/`. Supported formats: Parquet, JSON, CSV,
CSV folder, or HuggingFace cache.

---

## Note on Datasets

All LLM-generated code datasets used in the paper are included in the
`datasets/` folder. The pre-cached HuggingFace datasets required for Python 3
analysis (`datasets/hf_cache/`) are also included so no internet access is
needed at run time.

For large or third-party baseline datasets (e.g. MultiPL-T), refer to their respective original sources if you need to reproduce or extend the baseline analysis to suit your language.
