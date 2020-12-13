import requests

obl = ','.join([str(i) for i in range(1, 35)])
url = 'https://api.lardi-trans.com/v2/references/areas?ids=' + obl

respons = requests.get(url, headers={"Accept": "application/json", "Authorization": "2C3BC10BCBR000000197"})

data = respons.json()


def get_obl_by_id(id_number):
    for i in data:
        if i['id'] == id_number:
            return i['name']


print('Для выхода из программы используйте цифру 1')
while True:
    id = int(input('Введите id области от 15 до 39: '))
    if id == 1:
        print('Спасибо, до свидания)')
        break
    elif id not in range(15, 40):
        print('Нет такого id')

    else:
        print(get_obl_by_id(id))
