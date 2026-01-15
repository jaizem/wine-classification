#!/usr/bin/env bash

# Exit immediately if a command fails
set -e

# -------- CONFIG --------
PROJECT_NAME="wine_classification"
ENV_FILE="requirements.yml"
ENV_NAME="wine_classification"
PYTHON_VERSION="3.11"
# ------------------------

echo "Setting up $PROJECT_NAME environment..."

# Check for conda
if ! command -v conda &> /dev/null; then
    echo "Conda not found. Please install Miniconda or Anaconda first."
    exit 1
fi

# Initialize conda for this shell
eval "$(conda shell.bash hook)"

# Check if environment already exists
if conda env list | grep -q "^$ENV_NAME "; then
    echo "Conda environment '$ENV_NAME' already exists."
else
    echo "Creating conda environment '$ENV_NAME' from $ENV_FILE..."
    conda env create -f "$ENV_FILE"
fi

# Activate environment
echo "Activating environment '$ENV_NAME'..."
conda activate "$ENV_NAME"

# Verify Python version
echo "Python version:"
python --version

# Install project in editable mode (recommended for src/ layout)
if [[ -f "pyproject.toml" || -f "setup.py" ]]; then
    echo "Installing $PROJECT_NAME in editable mode..."
    pip install -e .
else
    echo "No pyproject.toml or setup.py found. Skipping editable install."
fi

echo "Setup complete."
echo "To activate later, run: conda activate $ENV_NAME"
