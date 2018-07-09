#!/usr/bin/python
#title                  :smeter-api.py
#description    :Script to make Smartmeter available over the network
#author                 :Rob Lensen
#date                   :20180709
#version                :0.1
#usage                  :python smeter-api.py.py
#notes                  :
#python_version :2.6.6
#==============================================================================

from flask import Flask
from flask_restplus import Resource, Api
from flask import make_response, Flask

from smeterd.meter import SmartMeter

meter = SmartMeter('/dev/cuaU0')

def output_plain(data, code, headers=None):
    resp = make_response(str(data ), code)
    resp.headers.extend(headers or {})
    return resp


app = Flask(__name__)
api = Api(app, default_mediatype='text/plain')
api.representations['text/plain'] = output_plain
@api.route('/smart')
class HelloWorld(Resource):
    def get(self):
        packet = meter.read_one_packet()
        return output_plain(packet, 200)
        
        meter.disconnect()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
