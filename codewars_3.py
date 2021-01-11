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
#
# def byn_search(a, value):
#    mid = len(a) // 2
#    low = 0
#    high = len(a) - 1
#
#    while a[mid] != value and low <= high:
#       if value > a[mid]:
#          low = mid + 1
#       else:
#          high = mid - 1
#       mid = (low + high) // 2
#
#    if low > high:
#       print("No value")
#    else:
#       print("ID =", mid)
#
# byn_search(['a', 'b', 'c', 'd', 'e', 'i', 'k'], 'a')
# #
#
# n = int(input())
#
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
#
# print(factorial)
#
#
# def find_smallest(arr):
#    smallest = arr[0]
#    smallest_index = 0
#    for i in range(1, len(arr)):
#       if arr[i] < smallest:
#          smallest = arr[i]
#          smallest_index = i
#    return smallest_index
#
# print(find_smallest([5, 1, 4,-4, 7, 2, 0, 6]))
#
# def selection_sort(arr):
#    new_sort = []
#    for _ in range(len(arr)):
#       numb = find_smallest(arr)
#       new_sort.append((arr.pop(numb))*2)
#    new_sort.reverse()
#
#    return new_sort
#
# print(selection_sort([5, 1, 4,-4, 7, 2, 0, 6]))
#
# x = (selection_sort([5, 1, 4,-4, 7, 2, 0, 6])).reverse()
# print(x)
# l = [5, 1, 4, -4, 7, 2, 0, 6]
# l.sort(reverse=True)
# print(l)
#
# def rec(x):
#     print(f'{x} first')
#     if not x:
#         return 0
#     else:
#
#         return x[0] + rec(x[1:])
#
# print(rec([7, 6]))

# def binary_search(arr, val):
#   left = 0
#   right = len(arr)-1
#   mid = (left + right)//2
#
#   if val == arr[mid]:
#      return mid
#   if val > arr[mid]:
#      return binary_search(arr[mid+1:], val) + (mid + 1)
#   return binary_search(arr[:mid], val)
#
# print(binary_search(['a', 'b', 'c', 'd', 'e', 'i', 'k'], 'c'))

