# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To allow requests from your frontend if it's on a different port/domain

@app.route('/api/greet', methods=['POST'])
def greet_user():
    data = request.get_json()
    name = data.get('name', 'stranger')
    return jsonify({
        'message': f'Hello, {name}! Welcome to the Flask API 😄'
    })

if __name__ == '__main__':
    app.run(debug=True)
