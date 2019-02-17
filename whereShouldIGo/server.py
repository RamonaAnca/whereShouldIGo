from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///travelling.db')
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from user")
        result = {'user': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result) 
		
class Username(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select username, password from user where idUser = ?",(employee_id,))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class LocationType(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from locationType")
        result = {'locationType': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result) 

		
api.add_resource(Users, '/user') # Route_1
api.add_resource(Username, '/user/<employee_id>') # Route_3
api.add_resource(LocationType, '/locationType') # Route_2

if __name__ == '__main__':
     app.run(port=5002)