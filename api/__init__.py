from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy

#Create an instance of Flask
app = Flask(__name__)

from . import config

db = SQLAlchemy(app) 
ma = Marshmallow(app)
api = Api(app)

from . import resourses

#connect api resources
api.add_resource(resourses.CO2_Telemetry, '/api/co2')
api.add_resource(resourses.CO2_all, '/api/co2/all')
api.add_resource(resourses.Humidity_all, '/api/humidity/all')
api.add_resource(resourses.Temperature_all, '/api/temperature/all')
api.add_resource(resourses.All_Telemetry, '/api/all')

