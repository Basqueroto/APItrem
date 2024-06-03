from flask import Flask, request, jsonify

app = Flask(__name__)

direcao = 'invertida'
controle = {'one': 'direita', 'two': 'direita', 'thre':'direita'}

@app.route('/', methods=['GET'])
def init ():
    return 'initial page'

@app.route('/ultraTrem', methods=['POST'])
def mandar ():
    Name = request.json.get('distance')
    print(Name)
    return 'success'
  
#mudar direcao
@app.route('/switchDirecao', methods=['POST'])
def switchDirecao ():
    estado = request.json.get('state')
    global direcao
    direcao = estado
    return jsonify({'status': 'success'})

@app.route('/mudarDirecao', methods=['POST'])
def mudarDirecao ():
    estado = request.json.get('state')
    if direcao != estado:
        return direcao
    return estado  

#mudar caminho
@app.route('/switchTrilho', methods=['POST'])
def switchTrilho ():
    estado = request.json.get('state')
    trilho = request.json.get('trilho')
    global controle

    controle[trilho] = estado
    return jsonify({'status': 'success'})

@app.route('/controleTrilhos', methods=['GET'])
def controleTrilhos ():
    return controle 


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)