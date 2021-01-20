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