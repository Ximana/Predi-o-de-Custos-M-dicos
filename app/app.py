from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Carregar o modelo
filename = 'modelo_Predicao_de_Custos_Medicos.pkl'
with open(filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Pegar os dados do formulário
        data = request.form

        # Extrair os dados do formulário e convertê-los para o tipo apropriado
        id_pedido = float(data['ID_Pedido'])
        data_pedido = float(data['Data_Pedido'])  # Supondo que você converta datas para um formato numérico apropriado
        id_cliente = float(data['ID_Cliente'])
        segmento = float(data['Segmento'])  # Transforme este campo adequadamente
        pais = float(data['Pais'])          # Transforme este campo adequadamente
        cidade = float(data['Cidade'])      # Transforme este campo adequadamente
        estado = float(data['Estado'])      # Transforme este campo adequadamente
        id_produto = float(data['ID_Produto'])
        categoria = float(data['Categoria'])  # Transforme este campo adequadamente
        subcategoria = float(data['SubCategoria'])  # Transforme este campo adequadamente

        # Prepare os dados para previsão
        input_data = np.array([[id_pedido, data_pedido, id_cliente, segmento, pais, cidade, estado, id_produto, categoria, subcategoria]])

        # Fazer a previsão
        prediction = model.predict(input_data)[0]

        # Retornar o resultado
        return render_template('index.html', prediction_text=f'Custo médico previsto: R${prediction:.2f}')
    except ValueError as e:
        return render_template('index.html', prediction_text=f'Erro na entrada dos dados: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
