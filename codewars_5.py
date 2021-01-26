# def by_in_int(arr):
#     s = 0
#     for digit in arr:
#         s = s * 2 + digit
#
#     return s
# print(by_in_int([1, 0, 1, 1]))
#
# def by_in_int1(arr):
#     return int("".join(map(str, arr)), 2)
#
# print(by_in_int1([1, 0, 1, 1]))
#
# def solution(s):
#     if len(s) % 2:
#         s = s+'_'
#     n = 2
#     res = [s[i:i+n] for i in range(0, len(s), n)]
#     return res
# print(solution('abcde'))

#
# def narcissistic(value):
#     return value == sum([int(i) ** len(str(value)) for i in str(value)])
#
#
# print(narcissistic(153))
#
# def capitals(word):
#     res = []
#     i =0
#     while i < len(word):
#         if word[i] == word[i].title():
#             res.append(i)
#         i += 1
#     return res
#
# print(capitals('CodCEWaWRs'))
#
# def iq_test(numbers):
#     list_numbers = numbers.split()
#     even_list = []
#     odd_list = []
#     for numb in list_numbers:
#         if int(numb) % 2 == 0:
#             even_list.append(numb)
#         else:
#             odd_list.append(numb)
#     if len(even_list) == 1:
#         return list_numbers.index(even_list[0]) + 1
#     else:
#         return list_numbers.index(odd_list[0]) + 1
#
#
#
#
# print(iq_test("2 4  8 10 7"))

# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

def expanded_form(num):
    pass
print(70304%100)
num = 70304
print(str(num)[1:])
l = len(str(num))
x = str(num)[0]
y = '0'*(l-1)
print(y)