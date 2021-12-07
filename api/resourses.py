from flask import jsonify, request
from flask_restful import Resource, abort

from . import models
from . import ma


class PostSchema(ma.Schema):
    class Meta:
        fields = ("value", "time_stamp", "mac")


json_schema = PostSchema()
jsons_schema = PostSchema(many=True)


def get_json_data(time_start=None, time_end=None):

    co2_all = models.CO2.query.order_by(models.CO2.time_stamp).all()
    temp_all = models.Temperature.query.order_by(
        models.Temperature.time_stamp).all()
    hum_all = models.Humidity.query.order_by(models.Humidity.time_stamp).all()

    co2_data, temp_data, hum_data = [], [], []
    for row in co2_all:
        co2_data.append(row.json())
    for row in temp_all:
        temp_data.append(row.json())
    for row in hum_all:
        hum_data.append(row.json())
    try:
        json_data = {
            "co2": co2_data,
            "temperature": temp_data,
            "humidity": hum_data
        }
    except:
        json_data = {'Error'}
    return jsonify(json_data)


class CO2_all(Resource):
    def get(self):
        telemetrics = models.CO2.query.all()
        # json_telemetrics = []
        # for row in telemetrics:
        #     json_telemetrics.append(row.json())
        # if not telemetrics:
        #     abort(404, message="Metric doesn't exist")
        # return jsonify(json_telemetrics)
        return jsons_schema.dump(telemetrics)


class Temperature_all(Resource):
    def get(self):
        telemetrics = models.Temperature.query.all()
        return jsons_schema.dump(telemetrics)


class Humidity_all(Resource):
    def get(self):
        telemetrics = models.Humidity.query.all()

        return jsons_schema.dump(telemetrics)


class CO2_Telemetry(Resource):
    def get(self):
        telemetry = models.CO2.query.first()
        if not telemetry:
            abort(404, message="Metric doesn't exist.")
        return jsonify(telemetry.json())

    def post(self):
        if request.method == "POST":
            telemetryData = request.get_json()
            telemetry = models.CO2(telemetryData['value'],
                                   telemetryData['time_stamp'],
                                   telemetryData['mac'])
            result = telemetry.create()
            return {'status': 'OK'}


class All_Telemetry(Resource):
    def get(self):

        all_telemetry = get_json_data()

        if not all_telemetry:
            abort(404, message="Metrics doesn't exist")
        return all_telemetry

    def post(self):
        if request.method == "POST":
            telemetryData = request.get_json()
            result = {}
            if "co2" in telemetryData:
                for row in telemetryData["co2"]:
                    telemetry = models.CO2(row['value'], row['time_stamp'],
                                           row['mac'])
                    result = telemetry.create()
            if "temperature" in telemetryData:
                for row in telemetryData["temperature"]:
                    telemetry = models.Temperature(row['value'],
                                                   row['time_stamp'],
                                                   row['mac'])
                    result = telemetry.create()
            if "humidity" in telemetryData:
                for row in telemetryData["humidity"]:
                    telemetry = models.Humidity(row['value'],
                                                row['time_stamp'], row['mac'])
                    result = telemetry.create()
            return result
