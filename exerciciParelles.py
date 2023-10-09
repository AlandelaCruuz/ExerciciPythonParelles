import csv

# EXERCICI 1    -LLegir el .CSV, guardar les dades en una llista de llistes y retornar per funció
def extract_all_tdata() -> list:
    players_list = []
    with open('basket_players.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
        for i,row in enumerate(reader):
            if i != 0:
                players_list.append(row)
    csv_file.close()
    return players_list

# EXERCICI 1.1    -Rep la primera fila en una llista i tradueix tots es valors de la llista
def title_dict(row) -> list:
    title_cat = {'Name' : 'Nom', 'Team' : 'Equip', 'Position' : 'Posicio', 'Heigth' : 'Altura', 'Weigth' : 'Pes', 'Age': 'Edat' }
    translated_row = []
    for word in row:
        if word in title_cat:
            word = title_cat[word]
            translated_row.append(word)
    return translated_row

# EXERCICI 1.2  -Rep una paraula (la Posicio del jugador) i retorna en String la traducció de l'anglès al català
def position_dict(word) -> str:
    positions_cat = {'Point Guard' : 'Base', 'Shooting Guard' : 'Escorta', 'Small Forward' : 'Aler', 'Power Forward' : 'Ala-pivot', 'Center' : 'Pivot'}
    return positions_cat[word]


# EXERCICI 1.3  -Rep la altura i pes en polzades i retorna una llista amb la altura i pes en Kilos i cm redondejats
def transform_data(height, weight) -> list:
    height = round(float(height)*2.54 , 2)
    weight = round(float(weight)*0.54 , 2)
    return ([height, weight])

# EXERCICI 1.4  -Transfomar les dades relatives a l'edat de decimals a enters
def transform_age(age) -> int:
    age = round(float(age))
    return (age)

def print_all_data():
    for i, row in enumerate(basket_players):
        print(i)

        row[2] = position_dict(row[2])
        row[3] = transform_data(row[3], row[4])[0]
        row[4] = transform_data(row[3], row[4])[1]
        row[5] = transform_age(row[5])
        print(row)

# EXERCICI 1.5  - Rep una llista dels jugadors i la guarda en un nou .CSV amb el delimitador '^' utilitzant un Diccionari
def save_players_list(players_list):
    mydict = {'Nom' : 'x', 'Equip' : 'x', 'Posicio' : 'x', 'Altura' : 'x', 'Pes' : 'x', 'Edat': 'x' }

    with open('jugadors_basket.csv', mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=mydict.keys(), delimiter="^")
            writer.writeheader()

            for row in players_list:
                data = {'Nom' : row[0], 'Equip' : row[1], 'Posicio' : row[2], 'Altura' : row[3], 'Pes' : row[4], 'Edat': row[5] }
                writer.writerow(data)
basket_players = extract_all_tdata()
save_players_list(basket_players)

# LLEGIR CSV I GUARDAR EN LLISTA
def extract_all_tdata() -> list:
    players_list = []
    with open('jugadors_basket.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter="^")
        for i,row in enumerate(reader):
            players_list.append(row)
    csv_file.close()
    return players_list

# EXERCICI 2.1 - Nom del jugador amb el pes més alt.
def heaviest_player(basket_players) -> str:
    #find the max value of the weight column just float values
    player = max(basket_players[1:], key=lambda weight: weight[4])
    return player

# EXERCICI 2.2 - Nom del jugador amb l'alçada més petita 
def minheightplayer(basket_players) -> str:
    nameplayer = ""
    minheight = float(basket_players[1][3])
    for row in basket_players[1:]:
        height = float(row[3])
        if minheight > height:
            minheight = height
            nameplayer = row[0]
    return print("El jugador amb l'alçada més petita és: "+nameplayer)



# EXERCICI 2.3 - Mitjana de pes i alçada de jugador per equip.
def average_physics_teams(basket_players) -> dict:
    teams = {}
    for row in basket_players[1:]:
        if row[1] not in teams: #Si el equipo NO esta en el diccionario como LLAVE lo añade junto con una lista de listas como valor
            teams[row[1]] = [[],[]]
            teams[row[1]][0].append(float(row[3]))
            teams[row[1]][1].append(float(row[4]))
        else:
            teams[row[1]][0].append(float(row[3]))
            teams[row[1]][1].append(float(row[4]))
    return teams

# EXERCICI 2.4 -Recompte de jugadors per posició.
def playersposition(basket_players):
    position_dict = dict()
    for row in basket_players:
        position = row[2]
        nameplayer = row[0]
        if position in position_dict:
            position_dict[position].append((nameplayer))
        else:
            position_dict[position] = [(nameplayer)]
    print(position_dict)
    for position, nameplayer in position_dict.items():
        totalplayers = len(nameplayer)        
        print(f"Posició: {position}, Jugadors: {totalplayers}")



# EXERCICI 2.5 - Distribució de jugadors per edat.
def age_players_count(basket_players)-> dict:
    ages = {}
    for row in basket_players[1:]:
        if row[5] not in ages:
            ages[row[5]] = 1
        else:
            ages[row[5]] += 1
    return ages

basket_players = extract_all_tdata()

print("MÉS PESAT: ", heaviest_player(basket_players)) # EXERCICI 2.1

minheightplayer(basket_players) # EXERCICI 2.2


team_keys = average_physics_teams(basket_players).keys() # EXERCICI 2.3

for i,team in enumerate(average_physics_teams(basket_players).values()):
    print("TEAM: ", list(team_keys)[i])
    print("HEIGHT: ", round(sum(team[0]) / len(team[0]), 2))
    print("WEIGHT: ", round(sum(team[1]) / len(team[1]), 2))
print("")

playersposition(basket_players) # EXERCICI 2.4

age = age_players_count(basket_players) # EXERCICI 2.5
print("EDAT | Nº Jugadors")
for i, a in enumerate(age):
    print(a,"  : ", age[a])

# EXERCICI 3.1 - LLegeix el csv i guarda les dades en un json
def csv_to_json():
    with open('jugadors_basket.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter="^")
        rows = list(reader)
    csv_file.close()
    with open('jugadors_basket.json', 'w') as json_file:
        json.dump(rows, json_file)
    json_file.close()
csv_to_json()
