# PredGly-CLI

A modern command-line interface for PredGly, a machine learning tool for predicting lysine glycation sites in homo sapiens proteins.

This project extends the original [PredGly](https://github.com/yujialinncu/PredGly) with a user-friendly CLI tool that provides:
- Direct protein sequence input (no file creation needed)
- Clean, modern command-line interface
- JSON output format for easy integration
- Cross-platform compatibility via conda environments

## Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/Hunter-Leo/PredGly-CLI.git
cd PredGly-CLI

# Create conda environment
mamba create -n predgly python=2.7 -y
mamba run -n predgly pip install numpy pandas matplotlib scipy scikit-learn click

# Install CLI tool
conda run -n predgly pip install -e .
```

### Usage Examples

#### Basic Prediction
```bash
conda run -n predgly predgly "MRALRAGLTLASGAGLGAVVEGWRRRREDARAAPGLLGRLPVLPVAAAAELPPVPGGPRGPGELAKYGLPGLAQLKSRESYVLCYDPRTRGALWVVEQLRPERLRGDGDRRECDFREDDS"
```

**Output:**
```
Predicted glycation sites:
--------------------------------------------------
Position   Amino Acid   Probability    
--------------------------------------------------
66         K            0.56711315329  
--------------------------------------------------
```

#### With Custom Threshold
```bash
conda run -n predgly predgly "PROTEIN_SEQUENCE" --threshold 0.7
```

#### Save Results to JSON
```bash
conda run -n predgly predgly "PROTEIN_SEQUENCE" --out results.json
```

**JSON Output Format:**
```json
{
  "sequence": "MRALRAGLTLASGAGLGAVVEGWRRRREDARAAPGLLGRLPVLPVAAAAELPPVPGGPRGPGELAKYGLPGLAQLKSRESYVLCYDPRTRGALWVVEQLRPERLRGDGDRRECDFREDDS",
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

#### No Results Found
When no glycation sites are predicted, an empty JSON `{}` is saved if `--out` is specified.

## CLI Options

- `SEQUENCE`: Protein sequence string (required)
- `--threshold, -t`: Probability threshold for prediction (default: 0.5)
- `--out, -o`: Output JSON file path (optional)
- `--help`: Show help message

## Features

✅ **Direct sequence input** - No need to create input files  
✅ **Modern CLI interface** - Built with Click framework  
✅ **JSON output** - Easy integration with other tools  
✅ **Flexible thresholds** - Customize prediction sensitivity  
✅ **Cross-platform** - Works via conda environments  
✅ **Backward compatible** - Original script still available  

## Requirements

- Python 2.7 (via conda environment)
- Dependencies: numpy, pandas, matplotlib, scipy, scikit-learn, click
- Conda or Mamba package manager

## Installation Details

See [INSTALL.md](INSTALL.md) for detailed installation instructions.

---

# Original PredGly Documentation

PredGly uses a machine learning method to predit lysine glycation sites for homo sapiens. Users can run program with specified protein sequences.

# Installation
* Install [Python 2.7](https://www.python.org/downloads/) in Linux and Windows.
* Because the program is written in Python 2.7, python 2.7 with the pip tool must be installed first. Glycation uses the following dependencies: numpy, pandas, matplotlib, scipy and scikit-learn. You can install these packages first, by the following commands:
```
pip install numpy
pip install pandas
pip install matplotlib
pip install scipy
pip install scikit-learn
```
* If you meet an error after inputting above commands in Linux, the specific contents are as follows:
</br>Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/sklearn'
Consider using the '--user' option or check the permissions.
</br>Users can change the commands into:
```
pip install numpy --user
pip install pandas --user
pip install matplotlib --user
pip install scipy --user
pip install scikit-learn --user
```

# Running PredGly
open cmd in Windows or terminal in Linux, then cd to the PredGly-master/codes folder which contains predict.py
</br>**For general glycation site prediction using our model, run:**
</br>`python predict.py -input [custom predicting data in txt format] -threshold [threshold value] -output [ predicting results in csv format]`  
</br>**Example:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5 -output ../codes/results.csv`
</br>-output is optional parameter, while -input and -threshold are required parameters. Prediction results will show in the cmd or terminal, and if you don't want to save results, you need not input -output.

</br>**Example:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5`

</br>**For details of -input,-threshold and -output, run:**
</br>`python predict.py -h`

# Announcements
* In order to obtain the prediction results, please save the query protein sequences and protein name in txt format. Users can refer to the example.txt under the codes folder. Also of note, each protein name should be added by '>', otherwise the program will occur error.
* The accepted amino acids are: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y, and a virtual amino acid O. If the protein fragments contain other amino acids, the program only will predict fragments which contain above-mentioned 21 amino acids. 
* To save the prediction results, the -ouput should be in csv format.
