from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

todos = {}

class Todo1(Resource):
    def get(self):
        return {'task' : 'Hello world'}
class Todo2(Resource):
    def get(self):
        return {'task' : 'Hello world'}, 201
class Todo3(Resource):
    def get(self):
        return {'task' : 'Hello world'}, 201, {'Etag' : 'some-opaque-string'}
# class HelloWorld(Resource):
#     def get(self):
#         return {'Hello':'world'}

api.add_resource(Todo1, '/<string:todo_id>')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
