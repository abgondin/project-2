import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Response,json
# from flask_cors import CORS, cross_origin
from flask import Flask, render_template

#################################################
# Connecting to postgresql database
#################################################

engine = create_engine("postgresql://iroikklkxnnpav:dccf35f488281d067a4a627232bff815d83fc0deb44ee26d5c0f59057331bbb2@ec2-54-167-152-185.compute-1.amazonaws.com:5432/dargfgk9hj0sjv")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

##Loading the scrapped data using CSV




#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'
#################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test", methods=["GET"])
def welcome():
    """List all available api routes."""
    
    #response = Response(json.dumps(new[0]), mimetype='application/json')
    #response = jsonify(results)
     #response.headers.add("Access-Control-Allow-Origin", "*")
    return (jsonify(new))


if __name__ == '__main__':
    # app.config['CORS_ALLOW_HEADERS'] = "Content-Type"
    # app.config['CORS_RESOURCES'] = {r"/api/*": {"origins": "*"}}
    app.run(debug=True)