from flask import Flask, jsonify
from flask_restful import Api, Resource
import functions
import json

with open('players.json', 'r') as players:
  data = json.load(players)

class JsonDataByCategory(Resource):
    def get(self, category):
        print("Received category:", category) 
        if category == 'players':
          return data
        elif category == 'ppg':
          return functions.sort_by_category(data,'ppg')     
        elif category == 'apg':
          return functions.sort_by_category(data,'apg')
        elif category == 'rpg':
          return functions.sort_by_category(data, 'rpg')
        elif category == 'orpg':
          return functions.sort_by_category(data, 'orpg')
        elif category == 'drpg':
          return functions.sort_by_category(data, 'drpg')
        elif category == 'bpg':
          return functions.sort_by_category(data, 'bpg')             
        elif category == 'spg':
          return functions.sort_by_category(data, 'spg') 
        elif category == 'tpg':
          return functions.sort_by_category(data, 'tpg')
        elif category == 'fpg':
          return functions.sort_by_category(data, 'fgp')
        elif category == 'fgpercent':
          return functions.sort_by_category(data, 'fgpercent')
        elif category == '3fgpercent':
          return functions.sort_by_category(data, '3fgpercent')
        elif category == 'ftpercent':
          return functions.sort_by_category(data, 'ftpercent')
        else:
          raise ValueError("Invalid category. Supported categories are 'ppg', 'apg', 'rpg', 'orpg', 'drpg', 'bpg', 'spg', 'tpg', 'fpg', 'fgpercent', '3fgpercent', and 'ftpercent'.")


with open('endpoints.json', 'r') as file:
  json_file = json.load(file)
  
class Endpoints(Resource):
  def get(self):
    return json_file