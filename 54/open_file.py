# with open('E:/udemypython/54/textt.txt') as auto_list:
#     text = auto_list.readlines()
#     for t in text:
#         print(t, end='')

# with open('E:/udemypython/54/textt.txt', 'a') as auto_list:
#     print('iiiiiii', file= auto_list)
import random, math

with open('numeral.txt', 'r') as num:
    # for _ in range(1, 10):
    #     number = (random.randint(1, 100))
    #     num.write(str(number) + "\n")

    with open('sort_numeral.txt', 'a') as append_number:
        for i in num:
            if int(i) % 2 == 0:
                append_number.write(i)

with open('sort_numeral.txt', 'r') as append_numb:
    numb_list = []
    for i in append_numb:
        numb_list.append(i.strip())
        number_dict = {int(i): int(math.pow(int(i), 2)) for i in numb_list}
    key_list = []
    for key in number_dict.values():
        key_list.append(key)
    print(key_list)
    print(number_dict)
    print(len(numb_list))