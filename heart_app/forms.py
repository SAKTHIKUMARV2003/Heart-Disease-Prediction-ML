from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label="Age")
    sex = forms.ChoiceField(label="Sex", choices=[(1, "Male"), (0, "Female")])
    cp = forms.IntegerField(label="Chest Pain Type")
    trestbps = forms.IntegerField(label="Resting Blood Pressure")
    chol = forms.IntegerField(label="Cholesterol")
    fbs = forms.ChoiceField(label="Fasting Blood Sugar", choices=[(1, "> 120 mg/dl"), (0, "≤ 120 mg/dl")])
    restecg = forms.IntegerField(label="Resting ECG")
    thalach = forms.IntegerField(label="Max Heart Rate")
    exang = forms.ChoiceField(label="Exercise Induced Angina", choices=[(1, "Yes"), (0, "No")])
    oldpeak = forms.FloatField(label="Oldpeak (ST Depression)")
    slope = forms.IntegerField(label="Slope of Peak Exercise")
    ca = forms.IntegerField(label="Number of Major Vessels")
    thal = forms.IntegerField(label="Thalassemia")
