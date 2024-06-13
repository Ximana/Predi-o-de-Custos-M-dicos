from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Carregar o modelo
with open('modelo_Predicao_de_Custos_Medicos.pkl', 'rb') as file:
    model = pickle.load(file)

# Carregar as colunas usadas durante o treinamento
with open('colunas_treinamento.pkl', 'rb') as file:
    treino_columns = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Pegar os dados do formulário
    data = request.form
    novos_dados = pd.DataFrame({
        'ID_Pedido': [data['ID_Pedido']],
        'Data_Pedido': [data['Data_Pedido']],
        'ID_Cliente': [data['ID_Cliente']],
        'Segmento': [data['Segmento']],
        'Pais': [data['Pais']],
        'Cidade': [data['Cidade']],
        'Estado': [data['Estado']],
        'ID_Produto': [data['ID_Produto']],
        'Categoria': [data['Categoria']],
        'SubCategoria': [data['SubCategoria']]
    })

    # Transformar variáveis categóricas em numéricas
    novos_dados = pd.get_dummies(novos_dados, drop_first=True)

    # Garantir que a ordem das colunas é a mesma que foi usada no treinamento
    novos_dados = novos_dados.reindex(columns=treino_columns, fill_value=0)

    # Fazer a previsão com o modelo treinado
    y_pred_novos_dados = model.predict(novos_dados)

    # Exibir a previsão
    prediction_text = f'Previsão de Valor de Venda: kz{y_pred_novos_dados[0]:.2f}'
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
