#Favorite APIs: Stripe, RemoveBG

from flask import Flask, jsonify, render_template
from flask_restful import Api, Resource
from resources.json_resource import JsonDataByCategory, Endpoints
from resources.csv_resource import CsvDataByCategory
import json
import functions
import file_conversions

from flask_cors import CORS

app = Flask(__name__)
api = Api(app)  
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

#JSON Endpoint
api.add_resource(JsonDataByCategory, '/json/<string:category>')
api.add_resource(Endpoints, '/endpoints')

#CSV Endpoints
api.add_resource(CsvDataByCategory, '/csv/<string:category>')




app.run(host='0.0.0.0', port=81)