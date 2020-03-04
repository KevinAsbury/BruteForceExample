from flask import Flask, request, jsonify

app = Flask(__name__)

PASSWORD = 'holmes'

@app.route('/login', methods=['POST'])
def login():
    content = request.get_json()
    password = content.get('password', '').strip()

    if password == PASSWORD:
        return jsonify('Success'), 200
    else:
        return jsonify('Unauthorized'), 401