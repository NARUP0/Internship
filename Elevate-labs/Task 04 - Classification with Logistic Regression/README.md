# Task 4 – Binary Classification with Logistic Regression

This project is part of the Elevate Labs AI & ML Internship.

## 📌 Objective
To build a binary classification model using **Logistic Regression** on the Breast Cancer Wisconsin Dataset.

## 🧰 Tools & Libraries
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## 📁 Dataset
[Breast Cancer Wisconsin Dataset – Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)

## 🔍 Steps Performed

1. **Data Loading & Cleaning**  
   - Removed null values  
   - Converted 'diagnosis' to numeric (M → 1, B → 0)

2. **Preprocessing**  
   - Split into training & testing sets  
   - Standardized features using `StandardScaler`

3. **Model Training**  
   - Used Logistic Regression from `sklearn.linear_model`

4. **Evaluation**  
   - Confusion Matrix  
   - Precision, Recall, F1-score  
   - ROC-AUC Score and ROC Curve

5. **Threshold Tuning**  
   - Explained the Sigmoid function  
   - Showed effect of changing threshold from 0.5 to 0.3

## 📈 Results

- ROC-AUC Score: ~0.98
- Good balance between precision and recall
- Custom threshold explored for better control

## ✅ Learnings

- Logistic regression for binary classification
- Importance of feature scaling
- Evaluation metrics (confusion matrix, ROC, precision/recall)
- Threshold tuning based on sigmoid outputs

