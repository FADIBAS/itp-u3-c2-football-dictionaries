def lists_to_dicts(squads_data):
    keys = ['number', 'position', 'name', 'date_of_birth', 'caps', 'club', 'country', 'club_country', 'year']
    
    players_as_dicts = []
    for player in squads_data:
        player_dict = {keys[i]: player[i] for i in range(len(keys))}
        players_as_dicts.append(player_dict)
    
    return players_as_dicts

# مثال
SQUADS_DATA = [
    ["1", "GK", "Juan Botasso", "(1908-10-23)23 October 1908 (aged 21)", "", "Quilmes", "Argentina", "Argentina", "1930"],
    ["9", "FW", "Roberto Cherro", "(1907-02-23)23 February 1907 (aged 23)", "", "Boca Juniors", "Argentina", "Argentina", "1930"]
]

players_as_dicts = lists_to_dicts(SQUADS_DATA)
print(players_as_dicts)

def group_by_position(squads_data):
    players_by_position = {}
    players_as_dicts = lists_to_dicts(squads_data)  # نستخدم الدالة من المهمة الأولى
    
    for player in players_as_dicts:
        position = player['position']
        if position not in players_by_position:
            players_by_position[position] = []
        players_by_position[position].append(player)
    
    return players_by_position

# اختبار
grouped_by_position = group_by_position(SQUADS_DATA)
print(grouped_by_position)


def group_by_country_and_position(squads_data):
    players_by_country = {}
    players_as_dicts = lists_to_dicts(squads_data)  # نستخدم الدالة من المهمة الأولى
    
    for player in players_as_dicts:
        country = player['country']
        position = player['position']
        
        if country not in players_by_country:
            players_by_country[country] = {}
        
        if position not in players_by_country[country]:
            players_by_country[country][position] = []
        
        players_by_country[country][position].append(player)
    
    return players_by_country

# اختبار
grouped_by_country_and_position = group_by_country_and_position(SQUADS_DATA)
print(grouped_by_country_and_position)


# قائمة اللاعبين الأصلية:
SQUADS_DATA = [
    ["1", "GK", "Juan Botasso", "(1908-10-23)23 October 1908 (aged 21)", "", "Quilmes", "Argentina", "Argentina", "1930"],
    ["9", "FW", "Roberto Cherro", "(1907-02-23)23 February 1907 (aged 23)", "", "Boca Juniors", "Argentina", "Argentina", "1930"],
    ["2", "DF", "Luis Monti", "(1901-05-15)15 May 1901 (aged 29)", "", "San Lorenzo", "Argentina", "Argentina", "1930"],
    ["3", "FW", "Leônidas da Silva", "(1913-09-06)6 September 1913 (aged 17)", "", "Vasco da Gama", "Brazil", "Brazil", "1930"]
]

print(lists_to_dicts(SQUADS_DATA))
print(group_by_position(SQUADS_DATA))
print(group_by_country_and_position(SQUADS_DATA))
