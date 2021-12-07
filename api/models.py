from datetime import datetime

from . import db


class Telemetry(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float())
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    mac = db.Column(db.String(100))

    def __init__(self, value, time_stamp, mac):
        self.value = value
        self.time_stamp = time_stamp
        self.mac = mac

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            result = {'Status': 'OK', 'message': 'Added to database'}
        except:
            db.session.rollback()
            result = {'Status': 'Error', 'message': 'Error adding to database'}
        return result

    def __repr__(self):
        return f'Time: {self.time_stamp}, Value: {self.value}.'

    def json(self):
        return {
            'time_stamp': self.time_stamp,
            'value': self.value,
            'mac': self.mac
        }


class CO2(Telemetry):
    __tablename__ = 'co2_telemetry'


class Humidity(Telemetry):
    __tablename__ = 'humidity_telemetry'


class Temperature(Telemetry):
    __tablename__ = 'temperature_telemetry'
