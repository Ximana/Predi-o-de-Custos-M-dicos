# Predição de Custos Médicos

Este projeto tem como objetivo desenvolver um modelo preditivo para estimar os custos médicos individuais com base em características demográficas e de saúde dos beneficiários. O modelo é construído utilizando técnicas de machine learning e é acompanhado por uma interface de usuário (UI) simples para simulação de custos médicos e uma API para integração com outros sistemas.

## Conteúdo do Repositório

- `data.csv`: Dataset utilizado para treinamento do modelo.
- `modelo_custos_medicos.pkl`: Modelo treinado serializado.
- `app.py`: Código Python para a aplicação da UI e da API.
- `requirements.txt`: Lista de pacotes Python necessários para executar o código.

## Etapas do Projeto

1. **Análise Exploratória de Dados (EDA)**:
   - Examine as características dos dados.
   - Verifique padrões e distribuições.
   - Identifique correlações entre variáveis.

2. **Pré-processamento dos Dados**:
   - Trate valores ausentes e outliers.
   - Converta variáveis categóricas em numéricas.
   - Normalize os dados se necessário.

3. **Treinamento do Modelo**:
   - Escolha e treine um modelo de regressão.
   - Avalie o desempenho do modelo utilizando métricas como RMSE e R².

4. **Criação da Interface de Usuário (UI)**:
   - Desenvolva uma UI simples para simular custos médicos.

5. **Integração via API**:
   - Crie uma API para permitir a comunicação com o modelo preditivo.

## Como Executar o Código

Para executar a aplicação localmente:

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/predicao-custos-medicos.git
```
2. Instale os pacotes necessários:

pip install -r requirements.txt

3. Execute a aplicação Flask:
```bash
python app.py
```

Acesse a interface de usuário em seu navegador: `http://localhost:5000`

## Exemplo de Uso

- Insira as informações necessárias (idade, gênero, BMI, etc.) na interface.
- Obtenha a estimativa de custos médicos com base nos dados inseridos.

## Contribuições

Contribuições são bem-vindas! Para sugestões, melhorias ou correções, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT) - veja o arquivo `LICENSE` para mais detalhes.

