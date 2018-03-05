from flask import Flask, render_template, request
from flask_restful import Resource, Api,reqparse
from flask_socketio import SocketIO, emit

app = Flask(__name__)
api = Api(app)

class simple_rest_test(Resource):
    def get(self):
        return {'hello': 'world'}

    def put(self):
        self.print_request(request)

    def post(self):
        self.print_request(request)

    def print_request(self,prequest):
        print("##### Method: %s #####"%request.method)
        print("Request form = %s"%request.form)
        print("Request Args = %s"%request.args)
        print("Json = %s"%request.get_json())
        print("###################")
        print("Headers = %s"%request.headers)
        socketio.emit('postput_received',request.get_json())    

@app.route("/web/")
def norest():
   return render_template('main.html')

socketio = SocketIO(app)

api.add_resource(simple_rest_test, '/')

if __name__ == '__main__':
    socketio.run(app,debug=True)
