# Task 5: Decision Trees and Random Forests

## Objective
The goal of this task was to understand and implement tree-based machine learning models— specifically Decision Trees and Random Forests — using the Heart Disease Dataset.

## What I Did

### 1. Data Loading & Exploration
- Loaded the dataset using pandas.
- Verified that there were no missing values.

### 2. Decision Tree Classifier
- Trained a basic Decision Tree model.
- Visualized the tree using `plot_tree`.
- Observed overfitting:
  - Training Accuracy: 1.00
  - Testing Accuracy: 0.9854
- Applied pruning with `max_depth=4`:
  - Pruned Training Accuracy: 0.8829
  - Pruned Testing Accuracy: 0.80

### 3. Random Forest Classifier
- Trained a Random Forest with 100 estimators.
- Results:
  - Training Accuracy: 1.00
  - Testing Accuracy: 0.9854

### 4. Feature Importance
- Top features influencing prediction:
  1. cp (chest pain type): 0.1351
  2. ca: 0.1273
  3. thalach: 0.1222
  4. oldpeak: 0.1219

### 5. Cross-Validation
- Performed 5-fold cross-validation.
- Scores: [1.0, 1.0, 1.0, 1.0, 0.9854]
- Average Accuracy: 0.9971

## Results Summary

| Model                  | Training Accuracy | Testing Accuracy |
|------------------------|-------------------|------------------|
| Decision Tree          | 1.0000            | 0.9854           |
| Pruned Decision Tree   | 0.8829            | 0.8000           |
| Random Forest          | 1.0000            | 0.9854           |
| Cross-Validation (RF)  | —                 | 0.9971           |

## Files Included
- `task05.ipynb` – Jupyter notebook with all code and outputs
- `heart.csv` – Dataset used
- `README.md` – This file

## Libraries Used
- pandas
- matplotlib
- scikit-learn

## Dataset Source
Heart Disease Dataset - [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

## Key Learnings
- How Decision Trees and Random Forests work
- Overfitting and pruning in tree models
- Interpreting feature importance
- Cross-validation for performance evaluation
