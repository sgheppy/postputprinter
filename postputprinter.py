from flask import Flask, render_template, request
from flask_restful import Resource, Api, reqparse
from flask_socketio import SocketIO, emit

import datetime
import json



import os

SRV_PORT = os.environ.get("POSTPUSTPORT",8051)
SRV_HOST = os.environ.get("POSTPUSHOST","0.0.0.0")
SRV_DEBUG = os.environ.get("POSTPUSDEBUG",False)

app = Flask(__name__)
api = Api(app)

class simple_rest_test(Resource):
    def get(self):
        return {'hello': 'world'}

    def put(self):
        self.print_request(request)

    def post(self):
        self.print_request(request)

    def print_request(self,request):
        print("##### Method: %s #####"%request.method)
        print("Json = %s"%request.get_json())
        print("environ = %s"%str(request.environ))

        now = datetime.datetime.now()


        formatted_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        socketio.emit('postput_received',[request.get_json(), request.method,str(formatted_timestamp),str(request.headers),str(request.environ.get("HTTP_ORIGIN",None))])    

@app.route("/web/")
def norest():
   return render_template('main.html')

socketio = SocketIO(app)

api.add_resource(simple_rest_test, '/')

if __name__ == '__main__':
    socketio.run(app,host=SRV_HOST, port=SRV_PORT,debug=SRV_DEBUG)
