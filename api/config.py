from api import app
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = JAWSDB_URL
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True