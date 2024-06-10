from flask import Flask, request, jsonify

import ddbb

app = Flask(__name__)
@app.route('/createSaurio', methods=['POST'])
def createSaurio():
    jsonSaurio = request.get_json()
    print(jsonSaurio)
    ddbb.createSaurio(jsonSaurio)
    return jsonify({"respuesta": "dino respuestaaa"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
