import requests
import json
import sqlite3


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
respons = requests.get(url, headers={"Accept": "application/json"},
                       params={
                           'format': 'geojson',
                           'starttime': '2020-01-21',
                           'endtime': '2020-01-23',
                           'latitude': '34',
                           'longitude': '118',
                           'maxradiuskm': '2000',
                           'minmagnitude': '1'
                       })

data = respons.json()
with open('file_json.json', 'w') as f:
    json.dump(data, f, indent=4)

conn = sqlite3.connect('usgs_db.db')
cursor = conn.cursor()
# cursor.execute("CREATE TABLE usgs (place TEXT, magnitude INTENGER);")
place_magn_list = []
for d in (data['features']):
    insert_query = "INSERT INTO usgs VALUES (?, ?);"
    cursor.execute(insert_query, (d["properties"]["place"], d["properties"]["mag"]))

cursor.execute("select * from usgs;")
count = 0
for row in cursor:
    count += 1
    print(f'{count}. {row}')

conn.commit()
conn.close()
