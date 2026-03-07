# Evironment var
To be to use the Open AI key more securely, you need to store in a session. In this frmework we use a SESSION var and os.getenv("OPENAI_API_KEY") to keep it hidden from the source code.
You simply need to: 
``` bash
export OPENAI_API_KEY=KEY
```

and then:
``` python
import os
os.getenv("OPEN_API_KEY")
```

# Requirements
- Python 3 (must be installed already)
- ANTLR 4

## 1. ANTLR
- Download ANTLR and export class:
    - cd /usr/local/lib
    - curl -O https://www.antlr.org/download/antlr-4.13.1-complete.jar
    - export CLASSPATH="/Users/david/__PYTHON/antlr/antlr-4.13.1-complete.jar:$CLASSPATH" 

## 2. Python virtual environment
- conda create -n "Exp02"
- conda activate Exp02

## 3. Install ANTLR4 and requirements
- pip install -r requirements.txt

# OPENAI key
- Read: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#saving-environment-variables
- The key must be set to be able to use with os.env.



# ANTLR

## How to generate parser
To generate the parser (only with visitor):
- bash ../antlr4.sh -Dlanguage=Python3 -visitor -no-listener ANTLRv4Lexer.g4 ANTLRv4Parser.g4

To look at the Parse Tree:
- bash ../grun.sh Calc declarationExpression -gui

## How to play with the AST examples
Execute:
python main.py t.expr

Change the code to calculate and print in t.expr

