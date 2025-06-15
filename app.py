from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password123':
        app.logger.info(f"Successful login for user: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        app.logger.warning(f"Failed login attempt for user: {username}")
        return jsonify({"message": "Login failed"}), 401

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)