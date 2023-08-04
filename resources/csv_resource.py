import csv
from flask import Flask
from flask_restful import Api, Resource
import functions

app = Flask(__name__)
api = Api(app)

file_path = 'players.csv'
data = []

with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        data.append(row)


def lists_to_csv(data):
    csv_data = ""
    for row in data:
        csv_data += ",".join(row) + "\n"
    return csv_data

csv_data = lists_to_csv(data)

class CsvDataByCategory(Resource):
    def get(self, category):
        print("Received category:", category)
        data = []
        if category == 'players':
          return csv_data
        elif category == 'ppg':
          return functions.csv_sort_by_category(data,'ppg')   
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
