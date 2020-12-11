import requests
import json
import sqlite3


def save_eartquakes(place_magnitude_list):
    conn = sqlite3.connect("earthquakes_db.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
    cursor.executemany("INSERT INTO earthquakes VALUES (?, ?)", place_magnitude_list)
    conn.commit()
    conn.close()


def select_all_earthquakes():
    conn = sqlite3.connect("earthquakes_db.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM earthquakes")
    data = cursor.fetchall()
    [print(row) for row in data]
    conn.commit()
    conn.close()


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

place_magn_list = []
for d in (data['features']):
    place_magn_list.append((d["properties"]["place"], d["properties"]["mag"]))

# save_eartquakes(place_magn_list)

select_all_earthquakes()