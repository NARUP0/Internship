# Task 7 – Support Vector Machines (SVM)

## 🧠 Internship Task – Elevate Labs

This project focuses on binary classification using Support Vector Machines (SVM) with both linear and non-linear (RBF) kernels. We also visualize decision boundaries, tune hyperparameters, and evaluate model performance.

---

## 📊 Dataset

We used the **Breast Cancer Wisconsin dataset**, available in `sklearn.datasets`. It contains 30 numeric features and a binary target:

- `target = 0` → Malignant
- `target = 1` → Benign

Dataset CSV: [`breast_cancer_dataset.csv`](breast_cancer_dataset.csv)

---

## 🚀 What I Did

1. Loaded and explored the dataset
2. Preprocessed and scaled the features using `StandardScaler`
3. Trained two SVM models:
   - Linear Kernel
   - RBF Kernel
4. Evaluated both models using:
   - Accuracy
   - Confusion Matrix
   - Classification Report
5. Visualized decision boundaries using a synthetic 2D dataset
6. Tuned hyperparameters (`C`, `gamma`) using `GridSearchCV`
7. Compared performance before and after tuning

---

## 📈 Results

| Model        | Accuracy |
|--------------|----------|
| Linear SVM   | ✅ ~97%  |
| RBF SVM      | ✅ ~98%  |
| Tuned RBF SVM| ✅ ~99%  |

📌 (Exact numbers may vary due to random state)

---

## 📦 Tools & Libraries

- Python
- scikit-learn
- matplotlib
- numpy
- pandas
- seaborn (optional, for better plots)

---

## 📁 Files Included

- `task07.ipynb` – full code notebook
- `breast_cancer_dataset.csv` – dataset in CSV form
- `README.md` – project documentation

---

## 🙋‍♂️ Author

NROUPSINH KALPESHSINGH GOHIL

Elevate Labs Internship  

---

## 📌 Note

This project was done as part of Elevate Labs’ AI/ML Internship – Task 7.  
Feel free to use it for learning or as a reference.

