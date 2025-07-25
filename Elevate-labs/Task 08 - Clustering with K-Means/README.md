# 🧠 Task 8 – K-Means Clustering | Elevate Labs Internship

## 📌 Objective
To apply K-Means Clustering on the Mall Customer dataset and segment customers based on their behavior.

## 📁 Dataset
**Mall_Customers.csv**  
Source: [Kaggle – Customer Segmentation Dataset](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

## 🧪 Steps Performed

1. **Loaded** the dataset using Pandas
2. **Cleaned** and dropped non-numeric columns (`CustomerID`, `Gender`)
3. **Scaled** the features using `StandardScaler`
4. **Applied PCA** to reduce data to 2D and visualize clusters
5. **Trained K-Means** algorithm with different values of `K` (1–10)
6. **Used Elbow Method** to find the optimal number of clusters (`K = 5`)
7. **Visualized clusters** based on `Annual Income` and `Spending Score`
8. **Evaluated clustering** using Silhouette Score

## 📊 Results

- **Optimal K**: 5 (found using Elbow Method)
- **Silhouette Score**: `0.408`
- **Clusters were visualized** clearly using Seaborn scatter plot

## 🔧 Tools & Libraries Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## ✅ Conclusion
The task was successfully completed. K-Means clustering segmented customers into meaningful groups based on spending and income behavior.

## 📎 Files Included
- `task08.ipynb` – Google colab notebook with all code & plots
- `Mall_Customers.csv` – Dataset used for clustering
- `README.md` – This file

