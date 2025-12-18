# Customer Churn Analysis and Prediction

A Python-based pipeline for exploring customer demographics and predicting churn using optimized K-Nearest Neighbors (KNN). This project automates data cleaning, generates comprehensive visualizations, and tunes a classification model to identify key churn drivers.

## Table of Contents
- [Overview](#overview)
- [Workflow](#workflow)
- [Key Visualizations](#key-visualizations)
- [Modeling & Performance](#modeling--performance)
- [Installation](#installation)
- [Usage](#usage)

---

## Overview
The project is divided into two main stages:
1.  **Exploration & Visualization:** Automated generation of statistical plots to understand feature distributions and their relationship with customer churn.
2.  **Predictive Modeling:** A machine learning pipeline that handles data preprocessing, hyperparameter tuning via GridSearchCV, and model evaluation.

## Workflow
1.  **Data Cleaning:** 
2.  **Exploratory Data Analysis (EDA):** 
3.  **Pipeline Construction:** 
4.  **Optimization:** 

## Key Data Features:


## Modeling & Performance
The model utilizes a **K-Nearest Neighbors** classifier optimized with the following parameters:
- **Scalers:** MinMaxScaler
- **Search Space:** $k \in [1, 75]$, weights (uniform/distance), metrics (euclidean/manhattan/hamming).
- **Evaluation:**
    - Accuracy score and Classification Report (Precision, Recall, F1).
    - Confusion Matrix 
    - Permutation Importance

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/Churn-Analysis.git

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn eli5
```

## Usage
Ensure your dataset is placed in `../data/customer_data.csv`.

### 1. Run Exploration
Generate all visual assets:
```bash
python exploration.py
```

### 2. Run Modeling
Train the model and output performance metrics:
```bash
python model.py
```

## License
Distributed under the MIT License. See `LICENSE` for more information.