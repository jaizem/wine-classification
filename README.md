# Wine Classification using KMeans & Hierarchical Clustering

## Overview
This project applies unsupervised clustering techniques to classify wine samples from the [UCI Wine Dataset](#data-source), based on their chemical composition. Using KMeans and agglomerative clustering, the goal is to segment the wines into three clusters corresponding to different grape varietals.

Key insights include:
- KMeans outperforms agglomerative clustering in both cluster separation and internal validation scores (Silhouette, Davies-Bouldin).
- PCA is used to visualize clusters and identify key chemical features that distinguish varietals.
- Clustering results align closely with known characteristics of Barolo, Barbera, and Grignolino wines.

For detailed methodology, visualizations, and evaluation metrics, see the full `report.md`.

## Dataset
This dataset contains the results of a chemical analysis of wines grown in the same region in Italy, but derived from three different cultivars (grape varieties). The analysis includes the quantities of 13 different chemical constituents found in each wine sample. These chemical properties can be useful for classification and clustering tasks, particularly to distinguish wines by cultivar based on their chemical composition.

Each record in the dataset corresponds to a single wine sample and includes the following 13 features:
- Alcohol
- Malic acid
- Ash
- Alcalinity of ash
- Magnesium
- Total phenols
- Flavanoids
- Nonflavanoid phenols
- Proanthocyanins
- Color intensity
- Hue
- OD280/OD315 of diluted wines
- Proline

### Data Source
The dataset used in this project was obtained from the UCI Machine Learning Repository:

Aeberhard, S. & Forina, M. (1992). Wine [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5PC7J

Donated by Riccardo Leardi (riclea@anchem.unige.it).

## Environment Setup

### Step-by-Step Instructions for the Environment

1. **Create a Conda Environment:**
   To set up the project environment, we will be using Conda. If you don't have Conda installed, you can install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual).

   Once Conda is installed, open a terminal (or Anaconda Prompt) and run the following command to create a new environment named `clustering`:

   ```bash
   conda env create -f requirements.yml
   ```
   This command will create a new environment and automatically install all the required dependencies listed in the requirements.yml file.

2. **Activate the Conda Environment:**
    After the environment is created, activate it by running:
    ```bash
    conda activate clustering
    ```
    This ensures that you are using the correct Python environment for the project.

3. **Install Dependencies (If Required):**
    If for any reason you need to install additional dependencies or update the environment later, you can use the following command:

    ```bash
    conda env update -f requirements.yml
    ```
    This will ensure that all dependencies are installed and up-to-date based on the requirements.yml file.

4. **Jupyter Notebook Setup (Optional):**
    Once the environment is activated, you can open a Jupyter Notebook to work on the project. Simply run the following command:

    ```bash
    jupyter notebook
    ```
    This will launch Jupyter in your default browser, and you can start working on the notebooks for the project.

## Installing Dependencies Using `requirements.yml`

To install the dependencies, you should have the `requirements.yml` file provided. It includes a list of all the necessary packages and versions for the project. Below is a breakdown of the key dependencies included in the `requirements.yml` file for setting up the environment.

### Dependencies Breakdown
1. Python 3.11
This project uses Python 3.11, compatible with all included libraries and offering improved performance and features over earlier versions.

2. Pandas, Numpy, and Scikit-learn
- Pandas: For structured data manipulation and analysis.
- Scikit-learn: Provides clustering algorithms (KMeans, Agglomerative), PCA, and clustering metrics (silhouette score, Davies-Bouldin score).

3. Matplotlib and Seaborn
- Matplotlib: Core library for creating static, animated, and interactive plots.
- Seaborn: Built on Matplotlib, it offers enhanced statistical plotting and improved aesthetics.

4. Jupyter
Jupyter Notebooks are used as the primary interface for data exploration, visualization, and reporting.

5. Code Quality Tools
- nbqa: Enables running code quality tools directly on Jupyter notebooks.
- black: A code formatter used to ensure consistent Python code style.
- flake8: A linting tool to identify potential syntax and style issues.

---

## Additional Notes

Once you've installed all dependencies and activated the environment, you can start using the Jupyter notebooks for further analysis.

The environment is already set up with the required libraries, so you should be good to go once you've activated it.

### Custom silhouette_plot.py Utility
Scikit-learn does not currently provide a built-in function for generating silhouette plots. While it offers the silhouette score and silhouette samples, users are expected to manually implement plotting logic.

Although external libraries such as yellowbrick offer silhouette plot wrappers, they introduce additional dependencies and abstract away key visualization logic that can be helpful for customization and learning.

**Why a Custom Module?**
To maintain transparency, flexibility, and reusability across notebooks, this project includes a custom utility file:
`silhouette_plot.py`

This file contains a reusable silhouette_plot() function that:
- Accepts clustering labels and features as input.
- Computes silhouette coefficients.
- Plots the silhouette values grouped by cluster.
- Adds a red dashed line to indicate the average silhouette score.

### Contribution to Scikit-learn
In an effort to improve usability, the silhouette_plot() function developed for this project was submitted as part of a feature request to Scikit-learn. The hope is that it will eventually be considered for inclusion in the official library, making silhouette visualization more accessible for the wider data science community.

### Usage
Ensure silhouette_plot.py is in the same directory as your notebooks or scripts, then import it as follows:

```python
from silhouette_plot import silhouette_plot
```
---

## Troubleshooting

If you encounter issues with package versions or missing dependencies, try updating the environment or installing the missing packages using `conda` or `pip`. For example:

### Using Conda:
```bash
conda install <package-name>
```

### Using Pip:
```bash
pip install <package-name>
```

If you're still having trouble, feel free to open an issue in the GitHub repository.

