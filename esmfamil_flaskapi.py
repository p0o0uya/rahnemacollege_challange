from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Endpoint01 - participants
@app.route('/participants', methods=['POST'])
def templates():
    if request.method=='POST':
    


# Endpoint02 - events
@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method=='GET':
        print('this is a get request')
        print(request.args)
        return jsonify({'method': 'GET', 'result': request.args})
    elif request.method=='POST':
        print('this is a post request')
        return {'method': 'POST', 'result': request.args}
    else:
        pass

# Endpoint03 - hosts
# Endpoint04 - guests






if __name__ == "__main__":
    app.run(host='0.0.0.0')