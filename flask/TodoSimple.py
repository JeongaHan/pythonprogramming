from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id : todos[todo_id]}
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
class HelloWorld(Resource):
    def get(self):
        return {'Hello':'world'}

api.add_resource(TodoSimple, '/<string:todo_id>')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
