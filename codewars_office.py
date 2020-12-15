# def open_or_senior(data):
#     categories = []
#     for i in data:
#         if i[0] >= 55 and i[1] > 7:
#             categories.append('Senior')
#         else:
#             categories.append('Open')
#
#     return categories
#
# print(open_or_senior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]))

# def delete_nth(order, max_e):
#     my_dict = {}
#     new_list = []
#     for n in order:
#         if n not in my_dict:
#             my_dict[n] = 1
#             new_list.append(n)
#         else:
#             if n in my_dict and my_dict[n] < max_e:
#                 my_dict[n] += 1
#                 new_list.append(n)
#
#     return new_list
#
#
# print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
#
# def odd_or_even(arr):
#     if sum(arr) % 2 == 0:
#         return "even"
#     else:
#         return "odd"
#
# print(odd_or_even([]))

# def get_count(input_str):
#     num_vowels = 0
#     for i in input_str:
#         if i in 'aeiou':
#             num_vowels += 1
#
#     return num_vowels
#
# def anagrams(word, words):
#
#     anagramm_list = []
#     index = 0
#     while index < len(words):
#         list_words = list(words[index])
#         list_word = list(word)
#         list_words.sort()
#         list_word.sort()
#         if list_word == list_words:
#             anagramm_list.append(words[index])
#         index += 1
#
#     return anagramm_list
#
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/python
# def zero(a='0'):
#     if a != '0':
#         if a[0] == '+':
#             return 0 + int(a[1])
#         if a[0] == '-':
#             return 0 - int(a[1])
#         if a[0] == '*':
#             return 0 * int(a[1])
#         if a[0] == '/':
#             return int(0 / int(a[1]))
#     else:
#         return '0'
#
#
# def one(a='1'):
#     if a != '1':
#         if a[0] == '+':
#             return 1 + int(a[1])
#         if a[0] == '-':
#             return 1 - int(a[1])
#         if a[0] == '*':
#             return 1 * int(a[1])
#         if a[0] == '/':
#             return int(1 / int(a[1]))
#     else:
#         return '1'
#
#
# def two(a='2'):
#     if a != '2':
#         if a[0] == '+':
#             return 2 + int(a[1])
#         if a[0] == '-':
#             return 2 - int(a[1])
#         if a[0] == '*':
#             return 2 * int(a[1])
#         if a[0] == '/':
#             return int(2 / int(a[1]))
#     else:
#         return '2'
#
#
# def three(a='3'):
#     if a != '3':
#         if a[0] == '+':
#             return 3 + int(a[1])
#         if a[0] == '-':
#             return 3 - int(a[1])
#         if a[0] == '*':
#             return 3 * int(a[1])
#         if a[0] == '/':
#             return int(3 / int(a[1]))
#     else:
#         return '3'
#
#
# def four(a='4'):
#     if a != '4':
#         if a[0] == '+':
#             return 4 + int(a[1])
#         if a[0] == '-':
#             return 4 - int(a[1])
#         if a[0] == '*':
#             return 4 * int(a[1])
#         if a[0] == '/':
#             return int(4 / int(a[1]))
#     else:
#         return '4'
#
#
# def five(a='5'):
#     if a != '5':
#         if a[0] == '+':
#             return 5 + int(a[1])
#         if a[0] == '-':
#             return 5 - int(a[1])
#         if a[0] == '*':
#             return 5 * int(a[1])
#         if a[0] == '/':
#             return int(5 / int(a[1]))
#     else:
#         return '5'
#
#
# def six(a='6'):
#     if a != '6':
#         if a[0] == '+':
#             return 6 + int(a[1])
#         if a[0] == '-':
#             return 6 - int(a[1])
#         if a[0] == '*':
#             return 6 * int(a[1])
#         if a[0] == '/':
#             return int(6 / int(a[1]))
#     else:
#         return '6'
#
#
# def seven(a='7'):
#     if a != '7':
#         if a[0] == '+':
#             return 7 + int(a[1])
#         if a[0] == '-':
#             return 7 - int(a[1])
#         if a[0] == '*':
#             return 7 * int(a[1])
#         if a[0] == '/':
#             return int(7 / int(a[1]))
#     else:
#         return '7'
#
#
# def eight(a='8'):
#     if a != '8':
#         if a[0] == '+':
#             return 8 + int(a[1])
#         if a[0] == '-':
#             return 8 - int(a[1])
#         if a[0] == '*':
#             return 8 * int(a[1])
#         if a[0] == '/':
#             return int(8 / int(a[1]))
#     else:
#         return '8'
#
#
# def nine(a='9'):
#     if a != '9':
#         if a[0] == '+':
#             return 9 + int(a[1])
#         if a[0] == '-':
#             return 9 - int(a[1])
#         if a[0] == '*':
#             return 9 * int(a[1])
#         if a[0] == '/':
#             return int(9 / int(a[1]))
#     else:
#         return '9'
#
#
# def plus(a):
#     return '+' + a
#
# def minus(a):
#     return '-' + a
#
# def times(a):
#     return '*' + a
#
# def divided_by(a):
#     return '/' + a
#
# print(eight(divided_by(three())))
#
#
# # https://www.codetd.com/en/article/7183730
#
# def validBraces(string):
#     brackets_open = '([{<'
#     brackets_closed = ')]}>'
#     stack = []
#     for brackets in string:
#         if brackets in brackets_open:
#             stack.append(brackets)
#         if brackets in brackets_closed:
#             if len(stack) == 0:
#                 return False
#             index = brackets_closed.index(brackets)
#             print(index, brackets)
#             open_bracket = brackets_open[index]
#             if stack[-1] == open_bracket:
#                 stack = stack[:-1]
#             else:
#                 return False
#     return (not stack)
#
#
# print(validBraces('(([{}]()))'))
#
# def validBraces_1(string):
#     brackets_open = '([{<'
#     brackets_closed = ')]}>'
#     stack = []
#     for brackets in string:
#         if brackets in brackets_open:
#             stack.append(brackets)
#         if brackets in brackets_closed:
#             if len(stack) == 0:
#                 return False
#             if brackets == ')' and stack[-1] == '(':
#                 stack.pop()
#             if brackets == '}' and stack[-1] == '{':
#                 stack.pop()
#             if brackets == ']' and stack[-1] == '[':
#                 stack.pop()
#             if brackets == '>' and stack[-1] == '<':
#                 stack.pop()
#     if len(stack) == 0:
#         return True
#     else:
#         return False
#
# print(validBraces_1('(([{}]())[])'))
#
# def validBraces_2(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0
#
# print(validBraces_2('((({{[]}}())))'))