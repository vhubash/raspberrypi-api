from api import app
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://zrrva3zwz4q7dssa:h3gvuwsje6uugiue@d3y0lbg7abxmbuoi.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/bajzsahu0ut67fla'
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True