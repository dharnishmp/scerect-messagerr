from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def encode(message):
    encoded = ""
    for char in message:
        encoded += chr(ord(char) + 3)
    return encoded

def decode(message):
    decoded = ""
    for char in message:
        decoded += chr(ord(char) - 3)
    return decoded

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    message = data['message']
    action = data['action']

    if action == "encode":
        result = encode(message)
    else:
        result = decode(message)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    