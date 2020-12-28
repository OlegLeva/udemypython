# pig_it('Hello world !')     # elloHay orldway !
# import string
#
#
# def pig_it(words):
#     new_string = ''
#     for word in words.split():
#         if word in string.punctuation:
#             new_string += word + ' '
#         else:
#             if word[-1] in string.punctuation:
#                 new_word = word[1:-1] + word[0] + "ay" + word[-1] + ' '
#                 new_string += new_word
#             else:
#                 new_word = word[1::] + word[0] + "ay" + ' '
#                 new_string += new_word
#     return new_string[:-1]
#
#
# print(pig_it('Hello, world ! erny, T rn'))

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python

#
# def alphabet_position(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     my_dict = {}
#     my_string = ''
#     for i, b in enumerate(alphabet, 1):
#         my_dict[b] = i
#
#     while text:
#         if text[0].isalpha():
#             my_string += str(my_dict[text.lower()[0]]) + ' '
#             text = text[1:]
#         else:
#             text = text[1:]
#     return my_string[:-1]
#
# print(alphabet_position("The sunset sets at twelve o' clock."))
#
# def make_readable(seconds):
#     a = seconds // 60
#     ss = seconds % 60
#     mm = a % 60
#     hh = a // 60
#     if hh > 99:
#         hh = 99
#     if ss < 10:
#         ss = "0" + str(ss)
#     if mm < 10:
#         mm = "0" + str(mm)
#     if hh < 10:
#         hh = "0" + str(hh)
#     return f'{str(hh)}:{str(mm)}:{str(ss)}'
#
# print(make_readable(86399))
# print(make_readable(0))
#
#
# def make_readable(seconds):
#     a = seconds // 60
#     ss = seconds % 60
#     mm = a % 60
#     hh = a // 60
#     if hh > 99:
#         hh = 99
#     if ss < 10:
#         ss = "0" + str(ss)
#     if mm < 10:
#         mm = "0" + str(mm)
#     if hh < 10:
#         hh = "0" + str(hh)
#     return str(hh)+':'+ str(mm)+':'+ str(ss)
# print(make_readable(86399))

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# https://www.codewars.com/kata/550f22f4d758534c1100025a/python
# from itertools import repeat
#
#
# def dirReduc(arr):
#     direction_of_travel = []
#     n = arr.count("NORTH")
#     s = arr.count("SOUTH")
#     w = arr.count("WEST")
#     e = arr.count("EAST")
#     diff_nord_south = n - s
#     if diff_nord_south > 0:
#         direction_of_travel.extend(repeat("NORTH", diff_nord_south))
#     if diff_nord_south < 0:
#         direction_of_travel.extend(repeat("SOUTH", -diff_nord_south))
#     diff_west_east = w - e
#     if diff_west_east > 0:
#         direction_of_travel.extend(repeat("WEST", diff_west_east))
#     if diff_west_east < 0:
#         direction_of_travel.extend(repeat("EAST", -diff_west_east))
#
#     return direction_of_travel
#
#
# print(dirReduc(['NORTH', 'NORTH', 'WEST', 'SOUTH', 'EAST']))

#
# def dirReduc_1(arr):
#     for i in arr:
#         if 'NORTH' in arr[:arr.index(i)] and i == 'SOUTH':
#             arr.remove('NORTH')
#             arr.remove('SOUTH')
#         elif 'SOUTH' in arr[:arr.index(i)] and i == 'NORTH':
#             arr.remove('SOUTH')
#             arr.remove('NORTH')
#         elif 'WEST' in arr[:arr.index(i)] and i == 'EAST':
#             arr.remove('WEST')
#             arr.remove('EAST')
#         elif 'EAST' in arr[:arr.index(i)] and i == 'WEST':
#             arr.remove('EAST')
#             arr.remove('WEST')
#     return arr
#
# print(dirReduc_1(['NORTH', 'NORTH', 'WEST', 'SOUTH', 'EAST']))

# def dirReduc_1(arr):
#     n, s, w, e = 'NORTH', 'SOUTH', 'WEST', 'EAST'
#     for i in arr:
#         if n in arr[:arr.index(i)] and i == s:
#             arr.remove(n)
#             arr.pop(arr.index(i))
#         elif s in arr[:arr.index(i)] and i == n:
#             arr.remove(s)
#             arr.pop(arr.index(i))
#     for i in arr:
#         if w in arr[:arr.index(i)] and i == e:
#             arr.remove(w)
#             arr.pop(arr.index(i))
#         elif e in arr[:arr.index(i)] and i == w:
#             arr.remove(e)
#             arr.pop(arr.index(i))
#     return (arr)
#
# print(dirReduc_1(['NORTH', 'NORTH', 'WEST', 'WEST', 'WEST']))

# def find_outlier(integers):
#     odd_list = []
#     even_list = []
#     for i in integers:
#         if i % 2 == 0:
#             even_list.append(i)
#         if i % 2 != 0:
#             odd_list.append(i)
#
#     if len(odd_list) == 1:
#         return odd_list[0]
#     else:
#         return even_list[0]
#
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([3, 1719, 19, 160, 11, 13, -21]))
#
# def solution(number):
#     new_list = []
#     for n in range(0,number):
#         if n % 3 == 0 or n % 5 == 0:
#             new_list.append(n)
#     return sum(new_list)
#
# print(solution(10))


#
# def is_valid_IP(strng):
#     my_list = strng.split('.')
#     for n in my_list:
#         if n == '' or n.isnumeric() == False or len(my_list) != 4 \
#                 or int(float(n)) not in range(0, 256) or len(n)>1 and n[0]=='0':
#             return False
#
#     return True
#
#
#
# print(is_valid_IP('129.d30.67.89'))

# def to_jaden_case(string):
#     return ' '.join(i.capitalize() for i in string.split())
#
#
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
# print(to_jaden_case('If Newborn Babies Could Speak They Would Be The Most Intelligent Beings On Planet Earth.'))
# print(to_jaden_case("People Tell Me To Smile I Tell Them The Lack Of Emotion In My Face Doesn't Mean I'm Unhappy"))

# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

# def product(numbers):
#     if numbers == [0]:
#         return [0]
#     if numbers == [None] or numbers == [] :
#         return None
#     else:
#         res = 1
#         for n in numbers:
#             res *= n
#         return res
#
# print(product([-2, 0, 7, 8]))
# print(product([None]))
# print(product([0]))
# print(product([]))

#

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
#
# def get_key(d, value):
#     name_list = []
#     for k, v in d.items():
#         if v == value:
#             name_list.append(k)
#     return name_list
#
# print(get_key(favorite_languages, 'python'))
# print(favorite_languages.values())
# revers_dict = {v: k for k, v in favorite_languages.items()}
# print(revers_dict)

# def duplicate_count(text):
#     x = set()
#     for t in text:
#         if text.lower().count(t) > 1:
#             x.add(t)
#     print(x)
#     return len(x)
#
# print(duplicate_count("aA11"))

# def abbrev_name(name):
#     lst = name.split()
#     return (lst[0][0]).upper() + "." + (lst[1][0]).upper()
#
# print(abbrev_name("Sam Harris"))

# https://www.codewars.com/dashboard

def to_camel_case(text):
    if text == '':
        return ''
    text_list = text.replace('-', ' ').replace('_', ' ').replace('/', ' ')
    text_list = text_list.split(' ')
    first_word = text_list[0]
    if text_list[0] == first_word.title():
        res = ''.join([w.title() for w in text_list])
        return res
    elif text_list[0] != first_word.title():
        res = text_list[0]
        res_2 = ''.join([w.title() for w in text_list[1:]])
        res += res_2
        return res


print(to_camel_case("The-stealth/warrior_uuu_kk"))
