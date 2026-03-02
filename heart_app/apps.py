from flask import Flask, request, render_template
import numpy as np
import pickle  # for loading your model

app = Flask(__name__)

# Load your actual model here
# model = pickle.load(open('heart_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form.get(f)) for f in [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ]]

    input_data = np.array([features])
    
    # Replace with: result = model.predict(input_data)
    # For testing, use mock prediction:
    result = [1] if features[0] > 50 else [0]  # Example rule

    output = 'Positive for Heart Disease' if result[0] == 1 else 'Negative for Heart Disease'
    return f"<h2>Prediction Result: {output}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
