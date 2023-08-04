import csv
import json
import xml.etree.ElementTree as ET
import functions
import csv
data = []

with open('players.csv', 'r') as c_file:
  reader = csv.reader(c_file)
  next(reader)

  for stat in reader:
    data.append(stat)

with open('players.xml', 'w') as x_file:
  pass


data = []
with open('players.csv', 'r') as c_file:
  reader = csv.reader(c_file)
  next(reader)

  for stat in reader:
    data.append(stat)

root = ET.Element("Players")
"""Rk,Player,Pos,Age,Tm,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS,Player-additional

"""
import xml.etree.ElementTree as ET


root = ET.Element("Players")

for player_data in data:  # Skip the header row
    player = ET.SubElement(root, "player")

    rank = ET.SubElement(player, "rank")
    rank.text = player_data[0]

    name = ET.SubElement(player, "name")
    name.text = player_data[1]

    stats = ET.SubElement(player, "stats")

    position = ET.SubElement(stats, "position")
    position.text = player_data[2]

    age = ET.SubElement(stats, "age")
    age.text = player_data[3]

    team = ET.SubElement(stats, "team")
    team.text = player_data[4]

    games = ET.SubElement(stats, "games")
    games.text = player_data[5]

    games_started = ET.SubElement(stats, "games_started")
    games_started.text = player_data[6]

    minutes_pg = ET.SubElement(stats, "minutes_pg")
    minutes_pg.text = player_data[7]

    field_goals = ET.SubElement(stats, "field_goals_pg")
    field_goals.text = player_data[8]

    field_goals_attempted = ET.SubElement(stats, "field_goals_attempted_pg")
    field_goals_attempted.text = player_data[9]

    field_goals_percent = ET.SubElement(stats, "field_goals_percentage")
    field_goals_percent.text = player_data[10]

    three_pointers_pg = ET.SubElement(stats, "three_pointers_pg")
    three_pointers_pg.text = player_data[11]

    three_pointers_attempted_pg = ET.SubElement(stats, "three_pointers_attempted_pg")
    three_pointers_attempted_pg.text = player_data[12]

    three_pointers_percent = ET.SubElement(stats, "three_pointers_percentage")
    three_pointers_percent.text = player_data[13]

    two_pointers_pg = ET.SubElement(stats, "two_pointers_pg")
    two_pointers_pg.text = player_data[14]

    two_pointers_attempted_pg = ET.SubElement(stats, "two_pointers_attempted_pg")
    two_pointers_attempted_pg.text = player_data[15]

    two_pointers_percent = ET.SubElement(stats, "two_pointers_percentage")
    two_pointers_percent.text = player_data[16]

    effective_field_goal_percent = ET.SubElement(stats, "effective_field_goal_percentage")
    effective_field_goal_percent.text = player_data[17]

    free_throws_pg = ET.SubElement(stats, "free_throws_pg")
    free_throws_pg.text = player_data[18]

    free_throws_attempted_pg = ET.SubElement(stats, "free_throws_attempted_pg")
    free_throws_attempted_pg.text = player_data[19]

    free_throw_percent = ET.SubElement(stats, "free_throw_percentage")
    free_throw_percent.text = player_data[20]

    offensive_rebounds = ET.SubElement(stats, "offensive_rebounds")
    offensive_rebounds.text = player_data[21]

    defensive_rebounds = ET.SubElement(stats, "defensive_rebounds")
    defensive_rebounds.text = player_data[22]

    total_rebounds = ET.SubElement(stats, "total_rebounds")
    total_rebounds.text = player_data[23]

    assists = ET.SubElement(stats, "assists")
    assists.text = player_data[24]

    steals = ET.SubElement(stats, "steals")
    steals.text = player_data[25]

    blocks = ET.SubElement(stats, "blocks")
    blocks.text = player_data[26]

    turnovers = ET.SubElement(stats, "turnovers")
    turnovers.text = player_data[27]

    personal_fouls = ET.SubElement(stats, "personal_fouls")
    personal_fouls.text = player_data[28]

    points = ET.SubElement(stats, "points")
    points.text = player_data[29]

# Create the ElementTree object
functions.indent(root)
tree = ET.ElementTree(root)

# Write the XML to a file
tree.write("output.xml", encoding="utf-8", xml_declaration=True)
