from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista em memória
mensagens = []

# Rota que recebe o webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    mensagens.append({
        "id": data.get("id"),
        "mensagem": data.get("mensagem")
    })
    return jsonify({"status": "Mensagem recebida"}), 201

# Rota que lista todas as mensagens
@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(mensagens)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
