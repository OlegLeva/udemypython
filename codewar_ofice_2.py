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

def dirReduc(arr):
    direction_of_travel = []
    if "NORTH" and "SOUTH" in arr:
        x = arr.count("NORTH")
        y = arr.count("SOUTH")
        print(x)


dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])