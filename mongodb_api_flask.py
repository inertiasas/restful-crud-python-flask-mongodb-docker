
from flask import Flask, Response
import json
from mongodb_api import MongoAPI

app = Flask(__name__)

@app.route('/')
def base():
	return Response(response=json.dumps({"Status": "UP"}),
		status=200,
		mimetype='application/json')

@app.route('/mongodb', methods=['GET'])
def mongo_read():
	data = request.json
	if data is None or data == {}:
		return Response(response=json.dumps({"Error": "Please provide connection information"}),
			status=400,
			mimetype='application/json')
	obj1 = MongoAPI(data)
	response = obj1.read()
	return Response(response=json.dumps(response),
		status=200,
		mimetype='application/json')

@app.route('/mongodb', methods=['POST'])
def mongo_write():
	data = request.json
	if data is None or data == {} or 'Document' not in data:
		return Response(response=json.dumps({"Error": "Please provide connection information"}),
			status=400,
			mimetype='application/json')
	obj1 = MongoAPI(data)
	response = obj1.write(data)
	return Response(response=json.dumps(response),
		status=200,
		mimetype='application/json')


if __name__ == '__main__':
	app.run(debug=True, port=5001, host='0.0.0.0')