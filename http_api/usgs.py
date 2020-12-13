import requests
import json

data_start = input('Введите дату начала периода в формате "ГГГГ-ММ-ДД": ')
data_end = input('Введите дату конца периода в формате "ГГГГ-ММ-ДД": ')
latit = input('Укажите широту, которая будет использоваться для поиска радиуса: ')
long = input('Укажите долготу, которая будет использоваться для поиска радиуса: ')
radius = input('Введите радиус зоны в км.: ')
magnitude = input('Укажите минимальную магнитуду: ')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
respons = requests.get(url, headers={"Accept": "application/json"},
                       params={
                           'format': 'geojson',
                           'starttime': data_start,
                           'endtime': data_end,
                           'latitude': latit,
                           'longitude': long,
                           'maxradiuskm': radius,
                           'minmagnitude': magnitude
                       })

data = respons.json()
# with open('file_json.json', 'w') as f:
#     json.dump(data, f, indent=4)
for n, d in enumerate(data['features'], 1):
    print(f'{n}. Place: {d["properties"]["place"]} Magnitude: {d["properties"]["mag"]}')
