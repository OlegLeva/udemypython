import requests

obl = ','.join([str(i) for i in range(1, 25)])
url = 'https://api.lardi-trans.com/v2/references/areas?ids=' + obl


respons = requests.get(url, headers={"Accept": "application/json", "Authorization": "2C3BC10BCBR000000197"})

data = respons.json()

for i in data:
    print(i)
