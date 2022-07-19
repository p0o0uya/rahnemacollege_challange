from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Endpoint01 - register
@app.route('/register', methods=['POST', 'GET'])
def templates():
    if request.method=='POST':
        pass

# Endpoint02 - submit
@app.route('/participants', methods=['POST', 'GET'])
def templates():
    if request.method=='POST':
        pass
    

# Endpoint03 - results
@app.route('/results', methods=['GET', 'POST'])
def events():
    if request.method=='GET':
        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0')