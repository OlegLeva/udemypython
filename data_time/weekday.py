from datetime import date

day = int(input('Введите день '))
mount = int(input('Введите месяц '))
year = int(input('Введите год '))

data_1 = date(year, mount, day)
print(data_1, data_1.isoweekday())