# def fizzbuzz(n):
#     l = list(range(1, n+1))
#     for i in l:
#         if i % 3 == 0 and i % 5 != 0:
#             l[l.index(i)] = 'Fizz'
#         elif i % 3 != 0 and i % 5 == 0:
#             l[l.index(i)] = 'Buzz'
#         elif i % 3 == 0 and i % 5 == 0:
#             l[l.index(i)] = 'FizzBuzz'
#     return l
#
# print(fizzbuzz(10))

# arr = ["h", 0, "l", "a"]
#
# p = ','.join([str(i) for i in arr])
# print(p)
#
# def remove_every_other(my_list):
#     return my_list[::2]
#
#
# print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#
# def high_and_low(numbers):
#     s = list(map(int, numbers.split(" ")))
#     return f"{max(s)} {min(s)}"
#
#
# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

# import string

#
# def is_pangram(s):
#     count = 0
#     for l in string.ascii_lowercase:
#         if l in s.lower():
#             count += 1
#     if count >= len(string.ascii_lowercase):
#         return True
#     else:
#         return False
#
#
# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


# def pattern(m):
#     n = m
#     if n <= 0:
#         return ''
#     numb = ''
#     string = ''
#     if len(numb) > 10:
#         for i in range(10):
#             string += f'{numb}\n'
#             numb = numb[:-1]
#     while n != 0:
#         numb += str(n)
#         n -= 1
#     while numb != str(m):
#         string += f'{numb}\n'
#         numb = numb[:-len(str(m))]
#
#     string += numb
#
#     return string
#

# def pattern(n):
#     return "\n".join(["".join([str(y) for y in range(n, x, -1)]) for x in range(n)])
# print(pattern(50))

# def high(x):
#     my_dict = {}
#     for i, j in enumerate(string.ascii_lowercase, 1):
#         my_dict[j] = i
#     list_count = []
#     for word in x.split():
#         count = 0
#         for w in word:
#             count += my_dict[w]
#         list_count.append(count)
#     index = list_count.index(max(list_count))
#     return x.split()[index]
#
#
# print(high('man i need a taxi up to ubud'))

#

# print(first_non_repeating_letter('abba'))

# v = 'asdffadsf'
# def solution(s):
#     if len(s) % 2:
#         s += '_'
#     res = []
#     while s:
#         res.append(s[0:2])
#         s = s[2:]
#     return res
#
# print(solution('asdffadsf'))
# s = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]

#
# def namelist(names):
#     my_list = []
#     for i in names:
#         my_list.append(i['name'])
#     if len(names) == 2:
#         return " & ".join(my_list)
#     if len(names) == 1:
#         return "".join(my_list)
#     if len(names) == 0:
#         return ""
#     else:
#         my_str = ", ".join(my_list[:-2])
#         my_str += f', {" & ".join(my_list[-2:])}'
#
#     return my_str
#
#
# namelist(s)
# def decodeMorse(morse_code):
#     code = {'A': '.-',     'B': '-...',   'C': '-.-.',
#             'D': '-..',    'E': '.',      'F': '..-.',
#             'G': '--.',    'H': '....',   'I': '..',
#             'J': '.---',   'K': '-.-',    'L': '.-..',
#             'M': '--',     'N': '-.',     'O': '---',
#             'P': '.--.',   'Q': '--.-',   'R': '.-.',
#             'S': '...',    'T': '-',      'U': '..-',
#             'V': '...-',   'W': '.--',    'X': '-..-',
#             'Y': '-.--',   'Z': '--..', '0': '-----',
#             '1': '.----',  '2': '..---',
#             '3': '...--',  '4': '....-',  '5': '.....',
#             '6': '-....',  '7': '--...',  '8': '---..',
#             '9': '----.'
#             }
#     morze_reverce = {v: k for k, v in code.items()}
#     res = []
#     res_2 = ''
#     for i in morse_code.split('  '):
#         for j in i.split():
#             res_2 += morze_reverce[j]
#         res.append(res_2)
#         res_2 = ''
#     return ' '.join(res)
#
# print(decodeMorse('.... . -.--   .--- ..- -.. .'))

# def order(sentence):
#     # if not sentence:
#     #     return ""
#     my_dict = {}
#     list_numb = []
#     list_res = []
#     for word in sentence.split():
#         for s in word:
#             if s.isdigit():
#                 my_dict[s] = word
#                 list_numb.append(s)
#     list_numb.sort()
#     for w in list_numb:
#         list_res.append(my_dict[w])
#     return ' '.join(list_res)
#
#
#
#
# print(order(""))

# def scramble(s1, s2):
#     for i in set(s2):
#         if s2.count(i) > s1.count(i):
#             return False
#     return True
#
# print(scramble('rkqowdl', 'world'))
#
# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
# alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alpha_down = 'abcdefghijklmnopqrstuvwxyz'
# print(alpha_up.index('S'))
# print(alpha_up.index('F'))
#
#
# import string
# def rot13(message):
#     alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     alpha_down = 'abcdefghijklmnopqrstuvwxyz'
#     res = ''
#     for i in message:
#         if i in alpha_up:
#             x = alpha_up.index(i)
#             if x < 13:
#                 res += alpha_up[x+13]
#             if x == 13:
#                 res += alpha_up[0]
#             if x > 13:
#                 res += alpha_up[x + 13 - len(alpha_up)]
#
#         if i in alpha_down:
#             x = alpha_down.index(i)
#             if x < 13:
#                 res += alpha_down[x+13]
#             if x == 13:
#                 res += alpha_down[0]
#             if x > 13:
#                 res += alpha_down[x + 13 - len(alpha_down)]
#     return res
#
#
#
# print(rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

def spin_words(sentence):
    res = []
    for i in sentence.split():
        if len(i) > 4:
            res.append((i[::-1]))
        else:
            res.append(i)
    return ' '.join(res)


print(spin_words("Hey fellow warriors"))