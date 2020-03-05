from flask import Flask, request, jsonify, abort

app = Flask(__name__)

PASSWORD = 'holmes'

# Make a post request with a json body:
#   {"password": "magic"}
@app.route('/login', methods=['POST'])
def login():
    content = request.get_json()
    # Check for invalid content
    if (PASSWORD not in content):
        abort(422)
    elif (type(content['password']) is not str):
        abort(422)

    # strip the '/r' off the end it was preventing
    # a positivie match
    password = content.get('password', '').strip()

    if password == PASSWORD:
        return jsonify('Success'), 200
    else:
        return jsonify('Unauthorized'), 401

    # This should be hashed in real life:
    #   import hashlib
    #   digest = hashlib.md5(content['password'].encode().hexdigest())
    #   Then compare the digest and the PASSWORD digest for equality.