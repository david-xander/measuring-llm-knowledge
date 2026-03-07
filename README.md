# How much does an LLM know about my programming language?

This repository contains the official framework for systematically evaluating the level of knowledge Large Language Models (LLMs) have about specific programming languages.

This framework uses **ANTLR-based syntactic analysis** to extract variables (keywords and grammar rules) from LLM-generated code. This allows for a "diagnostic" view of model proficiency, capturing latent knowledge even in code snippets that are not well-formed or fail to execute.

By analyzing these variables, the framework can identify "latent knowledge" and structural patterns even in code that fails to compile. This makes it a powerful diagnostic tool for:

- Evaluating LLM Proficiency: Moving beyond "pass/fail" to see what parts of a language a model understands.
- Dataset Audit: Identifying representativeness issues in datasets, such as those created via systematic translation (e.g., MultiPL-T), which may unintentionally limit the syntactic expressiveness of the target language.
- Scope Alignment: Comparing model performance against specific language subsets (e.g., DQL in SQL or Class Diagrams in PlantUML) to ensure evaluations match the intended use case.

## Key Features

* **Granular Metrics:** Measures Keyword/Rule Coverage and Production Validity.
* **Partial Knowledge Capture:** Analyzes syntactically invalid code to identify where a model’s knowledge fails.
* **Extensible:** Designed to work with any language that has an ANTLR grammar.
* **Automatic Reporting:** Generates a complete language coverage report as a Jupyter Notebook.

---

## Requirements

* **Python 3.x**
* **ANTLR 4**

### Installation

1. Clone this repository.
2. Install the necessary Python dependencies:

```bash
pip install -r requirements.txt

```

---

## Setup & API Keys

To use OpenAI or other LLM providers, you must store your API keys as environment variables for security. We recommend using a session variable:

**Terminal (Linux/macOS):**

```bash
export OPENAI_API_KEY='your-key-here'

```

The framework accesses these keys via:

```python
import os
os.getenv("OPENAI_API_KEY")

```

---

## How to Use the Framework

### 1. Inputs

The framework requires two main inputs:

* **Language Description:** An ANTLR parser and a language template.
* **Dataset:** A collection of code examples for your target language (Note: Datasets and generated examples are not included in this repository due to size/licensing).

### 2. Adding a New Language

To incorporate a new target language:

1. **Parser:** Generate your ANTLR parser (one-file or lexer/parser split).
2. **Template:** Duplicate an existing language folder and integrate your parser.
3. **Adaptation:** Change the **root rule** of the parser and adapt the execution/data-handling logic. Specific guidance is provided in the codebase templates.
4. **Scope (Optional):** You can manually or automatically (via LLM) define custom keyword lists or exclude specific tokens to narrow your research focus.

### 3. Execution

To compute the metrics for your language:

1. **Create a Run Script:** In the `run/` folder, create a new script (e.g., `run_my_language.py`) based on the provided examples.
2. **Point to Dataset:** Inside your script, provide the path to your dataset and call the API functions to extract features.
3. **Run:**

```bash
python run/your_language.py

```

### 4. Output

After execution, the framework automatically generates:

* **Analysis:** A `.ipynb` (Jupyter Notebook) in the `analysis/` folder containing the language coverage report.
* **Raw Data:** All extracted variables and features are saved in the `results/` folder.

---

## Note on Datasets

If you need to generate a new dataset of examples using an LLM, refer to the `generation/` folder. You can use the scripts there as a guide to prompt an LLM and save the resulting code examples as your input dataset.

