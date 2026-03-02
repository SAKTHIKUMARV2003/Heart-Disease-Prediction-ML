import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset (use any heart disease dataset)
df = pd.read_csv("heart_disease_ml/dataset.csv")

# Preprocess data
X = df.drop(columns=['target'])
y = df['target']

# Split into train-test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "heart_disease_ml/heart_model.pkl")
