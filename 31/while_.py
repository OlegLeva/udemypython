for number in range(1, 11):
    print('\U0001f600' * number)

x = 1
while x <= 10:
    print('\U0001f601' * x)
    x += 1

for numb in range(10):
    count = 0
    emoticons = ''
    while count <= numb:
        emoticons += '\U0001f608'
        count += 1
    print(emoticons)

for numb in range(10):
    emoticons = ''
    for x in range(numb + 1):
        emoticons += '\U0001f611'
    print(emoticons)
