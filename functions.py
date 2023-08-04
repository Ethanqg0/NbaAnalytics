#JSON Functions

def indent(elem, level=0):
    """Recursively add indentation to XML elements."""
    indent_size = 2  # Specify the number of spaces for each indentation level
    tab = " " * indent_size
    i = "\n" + level * tab
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + tab
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i + tab
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def sort_by_category(players, category):
    if category == 'ppg':
        key_function = lambda player: float(player['ppg'])
    elif category == 'apg':
        key_function = lambda player: float(player['assists/pg'])
        category = 'assists/pg'
    elif category == 'rpg':
        key_function = lambda player: float(player['total_rebounds/pg'])
        category = 'total_rebounds/pg'
    elif category == 'orpg':
        key_function = lambda player: float(player['offensive_rebounds/pg'])
        category = 'offensive_rebounds/pg'
    elif category == 'drpg':
        key_function = lambda player: float(player['defensive_rebounds/pg'])
        category = 'defensive_rebounds/pg'
    elif category == 'bpg':
        key_function = lambda player: float(player['blocks/pg'])
        category = 'blocks/pg'
    elif category == 'spg':
        key_function = lambda player: float(player['steals/pg'])
        category = 'steals/pg'
    elif category == 'tpg':
        key_function = lambda player: float(player['turnovers/pg'])
        category = 'turnovers/pg'
    elif category == 'fpg':
        key_function = lambda player: float(player['fouls/pg'])
        category = 'fouls/pg'
    elif category == 'fgpercent':
        key_function = lambda player: float(player['field_goals_percent'])
        category = 'field_goals_percent'
    elif category == '3fgpercent':
        key_function = lambda player: float(player['three_points_percent'])
        category = 'three_points_percent'
    elif category == 'ftpercent':
        key_function = lambda player: float(player['free_throws_percent'])
        category = 'free_throws_percent'
    else:
        raise ValueError("Invalid category. Supported categories are 'ppg', 'apg', 'rpg', 'orpg', 'drpg', 'bpg', 'spg', 'tpg', 'fpg', 'fgpercent', '3fgpercent', and 'ftpercent'.")

    # Sort the players based on the specified category
    sorted_players = sorted(players, key=key_function, reverse=True)

    # Create the result list with the selected fields
    result_list = []
    for player in sorted_players:
        selected_player = {
            "name": player['name'],
            category: player[category]
        }
        result_list.append(selected_player)

    return result_list


# functions.py

def csv_sort_by_category(players, category):
    header = players[0]
    category_index = header.index(category)

    key_function = lambda player: float(player[category_index])
    sorted_players = sorted(players[1:], key=key_function, reverse=True)
    return [header] + sorted_players


#___________



#CSV Functions

def csv_sort_by_category(players, category):
    if category == 'ppg':
        key_function = lambda player: float(player[29])
    elif category == 'apg':
        key_function = lambda player: float(player['assists/pg'])
        category = 'assists/pg'
    elif category == 'rpg':
        key_function = lambda player: float(player['total_rebounds/pg'])
        category = 'total_rebounds/pg'
    elif category == 'orpg':
        key_function = lambda player: float(player['offensive_rebounds/pg'])
        category = 'offensive_rebounds/pg'
    elif category == 'drpg':
        key_function = lambda player: float(player['defensive_rebounds/pg'])
        category = 'defensive_rebounds/pg'
    elif category == 'bpg':
        key_function = lambda player: float(player['blocks/pg'])
        category = 'blocks/pg'
    elif category == 'spg':
        key_function = lambda player: float(player['steals/pg'])
        category = 'steals/pg'
    elif category == 'tpg':
        key_function = lambda player: float(player['turnovers/pg'])
        category = 'turnovers/pg'
    elif category == 'fpg':
        key_function = lambda player: float(player['fouls/pg'])
        category = 'fouls/pg'
    elif category == 'fgpercent':
        key_function = lambda player: float(player['field_goals_percent'])
        category = 'field_goals_percent'
    elif category == '3fgpercent':
        key_function = lambda player: float(player['three_points_percent'])
        category = 'three_points_percent'
    elif category == 'ftpercent':
        key_function = lambda player: float(player['free_throws_percent'])
        category = 'free_throws_percent'
    else:
        raise ValueError("Invalid category. Supported categories are 'ppg', 'apg', 'rpg', 'orpg', 'drpg', 'bpg', 'spg', 'tpg', 'fpg', 'fgpercent', '3fgpercent', and 'ftpercent'.")

      # Sort the players based on the specified category
    sorted_players = sorted(players, key=key_function, reverse=True)

    return sorted_players
    # Create the result list with the selected fields
    result_list = []
    for player in sorted_players:
        result_list.append(player)

    return result_list
