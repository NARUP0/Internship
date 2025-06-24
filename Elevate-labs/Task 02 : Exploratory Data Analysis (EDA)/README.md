# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

## 📌 Overview

This project is part of Task 2 of the Elevate Labs AI & ML Internship.  
The goal was to explore and understand the Titanic dataset using statistics and visualizations.

---

## 📁 Dataset Used

- Source: [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- File name: `Titanic-Dataset.csv`

---

## 🛠️ Tools & Libraries

- Python (in Google Colab)
- Pandas
- Seaborn
- Matplotlib

---

## 📊 What I Did

1. **Loaded the dataset** and checked its structure using `.info()` and `.head()`.
2. **Generated summary statistics** with `.describe()` to understand distributions.
3. Plotted **histograms** and **boxplots** to visualize feature distributions and spot outliers.
4. Created a **correlation heatmap** to see how numerical features relate.
5. Used **pairplots** and **countplots** to analyze survival rates by different categories like gender and class.
6. Made simple inferences based on the visualizations.

---

## 🔍 Key Findings

- **Women and children** had noticeably higher survival rates.
- **1st class passengers** were more likely to survive than those in 2nd or 3rd class.
- Higher **fare values** were generally associated with higher survival chances.
- There are **outliers** in columns like `Fare` and `Age`.
- Features like `Cabin` had too many missing values and might need to be dropped or imputed.

---

## 🧠 Feature-Level Insights

- **Sex:** Females had a much higher survival rate than males.
- **Pclass:** Passengers in higher classes had better chances of survival.
- **Age:** Younger passengers, especially children, survived more.
- **Fare:** Paying more (likely for better class) had a positive impact on survival.
- **SibSp & Parch:** Moderate family size helped; large groups had lower survival rates.

---

## 📎 Files Included

- `task02.ipynb` – The Colab notebook with code and visualizations.
- `Titanic-Dataset.csv` – The dataset I used (uploaded via Colab).
- `README.md` – This file.

---

## ✅ Task Completed For

**Elevate Labs – AI & ML Internship**  
Task 2: Exploratory Data Analysis  
By: *Nroupsinh Gohil*  
Date: *24 June 2025*

---
