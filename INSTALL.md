# Installation Guide

## Project Repository
This is the CLI version of PredGly with modern command-line interface.
- Repository: https://github.com/Hunter-Leo/PredGly-CLI.git

## Prerequisites
- [Mamba](https://mamba.readthedocs.io/) or [Conda](https://docs.conda.io/en/latest/) package manager

## Environment Setup

### 1. Create Python 2.7 Environment
```bash
mamba create -n predgly python=2.7 -y
```

### 2. Install Dependencies
```bash
mamba run -n predgly pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ numpy pandas matplotlib scipy scikit-learn click
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Hunter-Leo/PredGly-CLI.git
cd PredGly-CLI
```

### 2. Install PredGly CLI Tool
```bash
# Activate the conda environment first
conda activate predgly

# Then install the CLI tool
cd PredGly-CLI
pip install -e .
```

Alternatively, you can install without activating the environment:
```bash
cd PredGly-CLI
conda run -n predgly pip install -e .
```

This will install the `predgly` command globally in your conda environment.

## Usage

### Command Line Interface
The CLI provides a modern interface for protein glycation site prediction:

```bash
# Basic usage
predgly "PROTEIN_SEQUENCE"

# With custom threshold
predgly "PROTEIN_SEQUENCE" --threshold 0.6

# Save results to JSON file
predgly "PROTEIN_SEQUENCE" --out results.json

# Using conda run from any directory
conda run -n predgly predgly "PROTEIN_SEQUENCE" --out results.json
```

### Legacy Usage (Original Script)
You can still use the original script directly:

```bash
cd codes
mamba run -n predgly python predict.py -input example.txt -threshold 0.5 -output results.csv
```

### Command Parameters
- `SEQUENCE`: Protein sequence string (required)
- `--threshold, -t`: Probability threshold for prediction (default: 0.5)
- `--out, -o`: Output JSON file path (optional)

### Output Format
The CLI outputs results in a clean table format to console and optionally saves to JSON:

```json
{
  "sequence": "PROTEIN_SEQUENCE",
  "threshold": 0.5,
  "results": [
    {
      "position": 66,
      "amino_acid": "K",
      "probability": 0.56711315329
    }
  ]
}
```

If no results are found, an empty JSON `{}` is saved when `--out` is specified.

### Input Format (Legacy Script)
For the original script, protein sequences must follow this format:
```
>protein_name
SEQUENCE
>another_protein
SEQUENCE
```

## Notes
- Each protein name must start with `>`
- Accepted amino acids: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y, O
- sklearn version compatibility warnings can be ignored
- The CLI automatically handles sequence formatting and temporary file creation
