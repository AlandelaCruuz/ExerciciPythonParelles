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
def transformdata(height, weight) -> list:
    height = round(float(height)*2.54 , 2)
    weight = round(float(weight)*0.54 , 2)
    return ([height, weight])

def print_all_data():
    for i, row in enumerate(basket_players):
        print(i)

        row[2] = position_dict(row[2])
        row[3] = transformdata(row[3], row[4])[0]
        row[4] = transformdata(row[3], row[4])[1]

        print(row)

basket_players = extract_all_tdata()
print_all_data()
