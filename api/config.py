import os
from api import app
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_CONN")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True