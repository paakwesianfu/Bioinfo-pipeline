# Bioinfo-pipeline
A pipeline developed to gain familiarity with Git and GitHub.

## Project Description
This project focuses on generating metadata for sequence data using a simple and reproducible bioinformatics pipeline. It is intended as a learning tool for:
- Version control with Git  
- Collaboration using GitHub  
- Basic pipeline development in bioinformatics  
- Automated metadata generation  

## Dependencies
All scripts require:
- Python 3.x (latest version recommended)

Optional:
- pip (Python package manager)  
- virtualenv (for isolated environments)  

## Installation

### Windows
1. Download Python from the official website: https://www.python.org/downloads/  
2. Run the installer  
3. Ensure that "Add Python to PATH" is selected  
4. Verify installation:
   ```bash
   python --version
   ```

### macOS
Option 1: Using Homebrew  
```bash
brew install python
```

Option 2: Official installer  
Download from: https://www.python.org/downloads/mac-osx/  

Verify installation:
```bash
python3 --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify installation:
```bash
python3 --version
```

## Getting Started

### Clone the repository
```bash
git clone https://github.com/your-username/bioinfo-pipeline.git
cd bioinfo-pipeline
```

### Create a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### Install dependencies (if applicable)
```bash
pip install -r requirements.txt
```

## Usage
Run the pipeline script:
```bash
python3 main.py
