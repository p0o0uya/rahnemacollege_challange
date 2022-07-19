from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Endpoint01 - register
@app.route('/register', methods=['POST'])
def templates():
    if request.method=='POST':
        pass

# Endpoint02 - submit
@app.route('/participants', methods=['POST'])
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