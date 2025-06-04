# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np  # Solo necesitamos NumPy para arrays

app = Flask(__name__)

# Cargar modelo al iniciar
modelo = None
label_encoders = None

def load_model():
    global modelo, label_encoders
    modelo = joblib.load('salidas/modelo_pedidos.pkl')
    label_encoders = joblib.load('salidas/label_encoders.pkl')

load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Convertir datos usando los encoders
        encoded_data = []
        for col in ["hora", "clima", "edad"]:
            encoded_data.append(label_encoders[col].transform([data[col]])[0])
        
        # Convertir a array de NumPy y predecir
        prediction = modelo.predict(np.array([encoded_data]))[0]
        
        return jsonify({
            'prediccion': prediction,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({'error': str(e), 'status': 'error'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)