# Heart-Disease-Prediction-ML
Heart Disease Prediction using Machine Learning
📌 Project Description

This project predicts the presence of heart disease using supervised Machine Learning algorithms based on patient medical parameters. The workflow includes data preprocessing, exploratory data analysis, feature selection, model training, and evaluation.

Multiple algorithms such as Logistic Regression, Decision Tree, Random Forest, and K-Nearest Neighbors (KNN) were implemented and compared. Among them, Random Forest achieved the highest accuracy. The final system accepts new patient input and predicts whether heart disease is present (1) or not (0).

Algorithms Used
1.Logistic Regression – Baseline classification model
2.Decision Tree Classifier – Rule-based learning
3.Random Forest Classifier – Ensemble learning (Best Performing Model)
4.K-Nearest Neighbors (KNN) – Distance-based classification

1. Random Forest achieved the highest accuracy among all models.

1️. Data Collection
Used heart disease dataset (medical parameters dataset).
Loaded dataset using Pandas.

2️. Data Preprocessing

Checked for missing values
Handled null values
Converted categorical values into numerical format
Feature scaling (if required)

3️. Exploratory Data Analysis (EDA)

Correlation heatmap

Distribution plots

Feature relationship analysis

Identified important features affecting heart disease

4️. Feature Selection
Selected relevant medical attributes:
Age
Sex
Chest Pain Type
Blood Pressure
Cholesterol
Maximum Heart Rate
ST Depression
Thalassemia
And others

5️. Data Splitting
Split dataset into:
Training set (80%)
Testing set (20%)

6️. Model Training
Trained models using:
Logistic Regression
Decision Tree
Random Forest
KNN

7️.Model Evaluation

Accuracy Score
Confusion Matrix
Classification Report
Compared performance of all algorithms

8️. Prediction System
Built a predictive system that:
Accepts new patient input
Predicts heart disease risk
Outputs 0 (No Disease) or 1 (Disease Present)

Technologies Used
Python
NumPy
Pandas
Matplotlib
Seaborn
Scikit-learn
Jupyter Notebook

🎯 Conclusion
This project demonstrates how Machine Learning can support early detection of heart disease and help healthcare professionals make informed decisions. Future improvements include deployment as a web application and integration with real-time medical data.
