with open('E:/udemypython/54/textt.txt') as auto_list:
    text = auto_list.readlines()
    for t in text:
        print(t, end='')

# with open('E:/udemypython/54/textt.txt', 'a') as auto_list:
#     print('iiiiiii', file= auto_list)