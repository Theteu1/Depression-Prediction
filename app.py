from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Carrega o modelo treinado
modelo = joblib.load('./modelo/modelo_depressao.pkl')

# Mapeia os hábitos alimentares manualmente (como foram codificados no LabelEncoder)
dieta_map = {
    'Saudável': 0,
    'Moderado': 1,
    'Ruim': 2,
    'Não Saudável': 3
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():
    try:
        dados = request.get_json()

        entrada = pd.DataFrame([{
            'Have you ever had suicidal thoughts ?': int(dados['thoughts']),
            'Financial Stress': int(dados['financial']),
            'Academic Pressure': int(dados['academic']),
            'Sleep Duration': int(dados['sleep']),
            'Family History of Mental Illness': int(dados['family']),
            'CGPA': float(dados['cgpa']),
            'Study Satisfaction': int(dados['satisfaction']),
            'Work/Study Hours': int(dados['hours']),
            'Dietary Habits': dieta_map[dados['diet']],
            'Age': int(dados['age'])
        }])

        pred = modelo.predict(entrada)[0]
        proba = modelo.predict_proba(entrada)[0][pred] * 100

        resultado = "Com sinais de depressão" if pred == 1 else "Sem sinais de depressão"

        return jsonify({
            'resultado': resultado,
            'probabilidade': round(proba, 2)
        })

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)



