"""Попросить помощь у Макса"""


# TODO: https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

# filename = 'bigbook.pdf'
# try:
#    with open(filename, encoding='utf-8') as f:
#       contents = f.read()
# except FileNotFoundError:
#    print(f"Sorry, the file {filename} does not exist.")
# else:
#    # Подсчет приблизительного количества строк в файле.
#    words = contents.split()
#    num_words = len(words)
#    print(f"The file {filename} has about {num_words} words.")

# def number(bus_stops):
#    count = 0
#    for x in bus_stops:
#       count += (x[0] - x[1])
#    return count
#
#
# print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))

# def is_isogram(string):
#    print(string.lower())
#    if len(string) == 0:
#       return True
#    for s in string.lower():
#       if string.lower().count(s) > 1:
#          return False
#    return True
#
#
# print(is_isogram("RoOm"))
#
# def find_even_index(arr):
#    i = 0
#    while i < len(arr):
#       if sum(arr[0:i]) == sum(arr[i + 1:]):
#          return i
#       i += 1
#    return -1
#
#
#
# print(find_even_index([1, 2, 3, 4]))
# print(find_even_index([20, 10, -80, 10, 10, 15, 35]))

# print ((2001-1) // 100 + 1)

#
# def is_square(n):
#    if n == 0:
#       return True
#    if n < 0:
#       return False
#    x = n ** 0.5
#    if x % int(x) != 0:
#       return False
#    return True
#
# import math
# def is_square1(n):
#     return n > -1 and math.sqrt(n) % 1 == 0
#
# print(is_square(13))


def increment_string(strng):
   str_part = ''
   int_part = ''
   for s in strng:
      if s.isdigit():
         int_part += s
      if s == '0':
         str_part += s
      if s.isalpha():
         str_part += s
   if int_part == '':
      return str_part + '1'
   res = str_part + str(int(int_part) + 1)
   if res[-1] == '0':
      res[-1] = '1'

   return res

# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python




print(increment_string("foobar00"))
