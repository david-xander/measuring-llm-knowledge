# Artifact Submission Template for SLE

## Author Information
- **Names:** (1) David Delgado, (2) Lola Burgueño, (2) Robert Clarisó
- **Affiliations:** (1) Universitat Oberta de Catalunya, (2) Universidad de Málaga
- **Emails:** ddelgadoc@uoc.edu, lolaburgueno@uma.es, rclasiso@uoc.edu

## Associated Paper Information
- **Title:** How much does an LLM know about my programming language?
- **Abstract:**

Large Language Models (LLMs) are increasingly used for code generation, yet their support for programming languages is uneven, particularly for low-resource languages and infrequently used language constructs. Existing evaluation methodologies primarily assess functional correctness through test execution, which fails to reveal blind spots in a model’s knowledge of a target language. In this paper, we introduce a systematic framework to identify and quantify the syntactic knowledge exhibited by an LLM with respect to a given programming language. We define syntactic coverage as a set of measurable indicators of how comprehensively language constructs are represented in datasets and generated code.

Our approach analyzes code snippets against grammatical rules and structural features to compute interpretable coverage metrics, detect underrepresented constructs, and expose gaps in language support. The proposed framework supports comparative analysis across datasets, languages, and models through an automated pipeline that produces actionable diagnostic reports. Our experimental results demonstrate that syntactic coverage analysis reveals substantial differences in language support that are not captured by functional correctness alone, enabling more informed model selection, benchmark design, and dataset improvement strategies.

## Documentation
- **Link to the code repository:** https://doi.org/10.5281/zenodo.19828964
- The artifact is a Python framework for evaluating LLM proficiency in programming languages using ANTLR-based syntactic analysis. It includes all code, pre-generated datasets, pre-compiled ANTLR grammars, and pre-cached HuggingFace datasets required to reproduce the paper results without internet access. See `README.md` for a full description of the artifact structure.

---

## Artifact Evaluation Environment

### System Specifications Used by Authors
- **Operating System:** macOS
- **CPU:** Apple Silicon
- **Memory:** 16 GB
- **Disk Space:** ~8 GB (image + outputs)
- **GPU (if applicable):** N/A

### Estimated Hardware Requirements for Evaluation
- **Minimum required CPU:** Any modern x86-64 or ARM64 CPU
- **Minimum required Memory:** 4 GB RAM
- **Minimum required Disk Space:** 10 GB free (Docker image ~6 GB + runtime outputs)
- **Minimum required GPU (if applicable):** None

### Compatibility Considerations
- **Known compatibility issues of the container/VM:** The Docker image is built on `python:3.11-slim` (Linux/amd64). On Apple Silicon (arm64) machines, Docker Desktop runs the image transparently via Rosetta 2 emulation — no changes needed. All ANTLR parsers are pre-compiled to Python; no Java runtime is required inside the container.

---

## Kick-the-Tires

This section verifies that all dependencies are correctly installed and that
the artifact runs end-to-end without errors, using OCL as a representative
single-language run.

### Steps to Perform a Quick Test

1. **Install Docker Desktop** (if not already installed):
   Download from https://www.docker.com/products/docker-desktop/ and start it.
   Verify with:
   ```bash
   docker --version
   ```

2. **Build the Docker image** from the project root:
   ```bash
   bash docker-build.sh
   ```
   This builds the `sle2026-artifact` image locally (~5–10 minutes depending on
   hardware). All dependencies and datasets are bundled; no internet access is
   needed after the build.

3. **Run the kick-the-tires command:**
   ```bash
   bash docker-run-reduced.sh
   ```

### Expected Output

The command runs the following pipeline for OCL:

1. Keyword and syntactic analysis over the OCL datasets (baseline + 6 LLM-generated datasets).
2. Generation of `analysis/ocl.ipynb` (the OCL analysis notebook).
3. Execution of `analysis/ocl.ipynb` via `nbconvert`.

At the end of a successful run, the terminal prints:

```
  [ocl] Done.
...
============================================================
Everything went perfectly!
Now, let's execute the generated notebooks...
============================================================
  [ocl] Executing notebook: .../analysis/ocl.ipynb
...
All done.
```

Two host-side directories are populated:

- `results/ocl/` — raw CSV files with keyword frequencies and syntactic metrics
  for each OCL dataset.
- `analysis/ocl.ipynb` — a fully executed Jupyter notebook with all OCL
  coverage report (including charts, heatmaps, etc.).
- `analysis/4_usage_ocl.pdf` - the Figure 2 of our research paper.

### Troubleshooting

| Symptom | Likely cause | Solution |
|---|---|---|
| `command not found: docker` | Docker Desktop not installed or not running | Install Docker Desktop and ensure the daemon is running (whale icon in menu bar) |
| `pull access denied for sle2026-artifact` | Image has not been built yet | Run `bash docker-build.sh` first |
| `No space left on device` during build | Insufficient disk space | Free at least 10 GB and retry |
| Notebook execution fails with `ModuleNotFoundError` | Dependency missing from image | Rebuild the image; the `requirements-docker.txt` file should include all needed packages |
| `results/` or `analysis/` are empty after the run | Volume mount path mismatch | Ensure you run the shell scripts from the **project root** directory |

---

## Full Evaluation

### Reproduction Steps

All paper claims can be reproduced with a single command run from the project root:

```bash
bash docker-run.sh
```

This executes the complete pipeline:

1. Keyword and syntactic analysis for all six languages (OCL, PlantUML, Python 3, R, Lua, SQL).
2. Generation and execution of one Jupyter notebook per language under `analysis/`.
3. Execution of `analysis/_all_together.ipynb`, which aggregates results across
   all languages and writes the paper's main output files.


At the end of a successful run, the terminal prints:

```
============================================================
Everything went perfectly!
Now, let's execute the generated notebooks...
============================================================
  [lua] Executing notebook: /artifact/analysis/lua.ipynb
  [ocl] Executing notebook: /artifact/analysis/ocl.ipynb
  [plantuml] Executing notebook: /artifact/analysis/plantuml.ipynb
  [python3] Executing notebook: /artifact/analysis/python3.ipynb
  [r] Executing notebook: /artifact/analysis/r.ipynb
  [sql] Executing notebook: /artifact/analysis/sql.ipynb
============================================================
Now, let's execute the notebook that sum up all the results and generates the MAIN result table...
============================================================
Executing notebook: /artifact/analysis/_all_together.ipynb

All done.
```


### Expected Output

After `bash docker-run.sh` completes successfully:

- `results/<language>/` — CSVs with raw keyword frequencies, syntactic validity
  metrics, and rule usage vectors for every dataset of every language.
- `analysis/<language>.ipynb` — fully executed notebook for each of the six languages.
- `analysis/_all_together.ipynb` — fully executed combined notebook.
- `analysis/4_usage_ocl.pdf` — paper Figure 4 (OCL).
- `analysis/4_usage_python.pdf` — paper Figure 4 (Python 3).
- `analysis/rq1_table.json` — paper RQ1/RQ2 table data.
- `analysis/rq3_table.json` — paper RQ3 table data.


**The specific paper outputs produced are:**

| File | Paper location |
|---|---|
| `analysis/4_usage_ocl.pdf` | Figure 2 — OCL keyword usage heatmap |
| `analysis/4_usage_python.pdf` | Figure 3 — Python 3 keyword usage heatmap |
| `analysis/rq1_table.json` | Table 2 - main results table |
| `analysis/rq3_table.json` | Table 3 -  baseline dataset results table |

All remaining figures (coverage bar charts, frequency heatmaps, variance
plots, rule-usage heatmaps) are rendered as inline outputs within the
per-language notebooks (`analysis/ocl.ipynb`, `analysis/python3.ipynb`,
`analysis/plantuml.ipynb`, `analysis/r.ipynb`, `analysis/lua.ipynb`,
`analysis/sql.ipynb`). All of them are the corresponding Language coverage reports, mentioned in Figure 1 (green box) and described in Section 2 (Framework).

> **Note:** Every {LANGUAGE}.ipynb file contains many more specific figures that are not shown in the paper. But, they form part of the Language coverage report.

You can open the notebooks after execution in Jupyter (assuming you have installed it):
```bash
jupyter notebook analysis/
```

Or double-click them if you have VSCODE or any tool alike that allows Jupyter Notebook editing without the Jypyter environment.



### Estimated Runtime

| Run | Command | Estimated time |
|---|---|---|
| Kick-the-tires (OCL only) | `bash docker-run-reduced.sh` | ~5 minutes |
| Full run (all languages) | `bash docker-run.sh` | ~90–120 minutes |

Times vary depending on hardware.

### Potential Issues

**`_all_together.ipynb` fails to execute:**
This notebook loads results from all six languages. If any per-language
analysis failed or was interrupted, the combined notebook will raise a
`FileNotFoundError`. Solution: ensure the full run completes without errors
before inspecting `_all_together.ipynb`.

**PDF figures are not produced:**
The `.pdf` files are saved by `matplotlib` during notebook execution. If
`nbconvert` exits with a non-zero return code, the notebook cells that save
PDFs may not have run. Check the terminal output for `WARNING: nbconvert exited
with code <N>` and inspect the notebook for cell-level errors.

**Results differ slightly from the paper:**
LLM-generated datasets are fixed and bundled in `datasets/`, so analysis
results are deterministic. Any deviation from the paper values would indicate
an environment or dependency issue — rebuilding the Docker image from scratch
resolves most such cases.
