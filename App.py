from flask import Flask, jsonify
from control.IdadeController import IdadeController

app = Flask("API Idade")

# Função auxiliar para lidar com validações
def handle_validation_error(e):
    return jsonify({"erro": str(e)}), 400

# Endpoint GET: /idade/tempo/<int:idade>
@app.route('/idade/tempo/<int:idade>', methods=['GET'])
def get_tempo_de_vida(idade):
    try:
        idadeController = IdadeController()
        idadeController.idade_converter.idade = idade

        dias = idadeController.calcular_dias()
        horas = idadeController.calcular_horas()
        minutos = idadeController.calcular_minutos()
        segundos = idadeController.calcular_segundos()

        jsonResposta = {
            "idade": idade,
            "dias": dias,
            "horas": horas,
            "minutos": minutos,
            "segundos": segundos
        }
        return jsonify(jsonResposta), 200
    except ValueError as e:
        return handle_validation_error(e)

# Inicia o servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
