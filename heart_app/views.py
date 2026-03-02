from django.shortcuts import render
import os
import joblib
import numpy as np
import pandas as pd
from .forms import HeartDiseaseForm
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
import matplotlib
matplotlib.use("Qt5Agg")  # Use Qt instead of Tk
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64
from sklearn.metrics import roc_curve, auc
from django.http import HttpResponse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "heart_app/heart_disease_ml", "heart_model.pkl")
model = joblib.load(MODEL_PATH)

# Dummy test dataset (Replace with real test data for evaluation)
X_test = np.random.randint(20, 80, size=(50, 13))  # Simulated feature set
y_test = np.random.randint(0, 2, size=(50,))  # Simulated labels
y_pred = model.predict(X_test)

# Compute performance metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

def plot_confusion_matrix(conf_matrix):
    plt.figure(figsize=(6,4))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["No Disease", "Disease"], yticklabels=["No Disease", "Disease"])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return "data:image/png;base64," + base64.b64encode(image_png).decode()

conf_matrix_img = plot_confusion_matrix(conf_matrix)

def predict(request):
    form = HeartDiseaseForm()

    if request.method == "POST":
        # Get input features from form
        features = [float(request.POST.get(f'feature{i}', 0)) for i in range(1, 14)]
        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]
        prediction_label = "Positive (Heart Disease)" if prediction == 1 else "Negative (No Heart Disease)"

        # Generate Performance Metrics (Sample values, replace with actual calculations)
        accuracy = 0.91
        precision = 0.89
        recall = 0.85
        f1_score = 0.87
        roc_auc = 0.92

        # Generate Confusion Matrix (Dummy example, replace with actual y_test, y_pred)
        y_test = np.random.randint(0, 2, 100)
        y_pred = np.random.randint(0, 2, 100)
        cm = confusion_matrix(y_test, y_pred)

        plt.figure(figsize=(5, 4))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")
        conf_matrix_path = "heart_app/static/images/conf_matrix.png"
        plt.savefig(conf_matrix_path)
        plt.close()
        conf_matrix_paths = "static/images/conf_matrix.png"
        # Generate ROC Curve
        fpr, tpr, _ = roc_curve(y_test, y_pred)
        roc_auc_score = auc(fpr, tpr)

        plt.figure(figsize=(6, 5))
        plt.plot(fpr, tpr, color="blue", lw=2, label="ROC curve (area = {:.2f})".format(roc_auc_score))
        plt.plot([0, 1], [0, 1], color="gray", linestyle="--")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title("ROC-AUC Curve")
        plt.legend(loc="lower right")
        roc_curve_path = "heart_app/static/images/roc_curve.png"
        plt.savefig(roc_curve_path)
        plt.close()
        roc_curve_paths= "static/images/roc_curve.png"

        return render(request, "result.html", {
            "result": prediction_label,
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1_score,
            "roc_auc": roc_auc_score,
            "conf_matrix_img": "/" + conf_matrix_paths,
            "roc_curve_img": "/" + roc_curve_paths
        })
    return render(request, "prediction.html", {"form": form})

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')


