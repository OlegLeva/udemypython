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
#
# def expanded_form(num):
#     list_num = list(str(num))
#
#     result = []
#     while list_num:
#         l = len(list_num)
#         if list_num[0] == '0':
#             list_num.pop(0)
#         else:
#             x = list_num.pop(0)
#             result.append(x+'0'*(l-1))
#     return ' + '.join(result)
#
# print(expanded_form(70304))
#
#
# def sum_pairs(lst, s):
#     cache = set()
#
#     for i in lst:
#         print(cache)
#         if s - i in cache:
#             return [s - i, i]
#         cache.add(i)
#
#
#
#
# print(sum_pairs([10, 5, 2, 3, 7, 5], 10))

# def solve(st,k):
#     for l in sorted(st)[:k]:
#         st=st.replace(l,'',1)
#     return st
#
# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     else:
#         for l in cc[:len(cc)-4]:
#             cc = cc.replace(l, '#', 1)
#     return cc
#
# print(maskify('ib'))
#
#
# print(solve('abracadabra', 6))
#
# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]
#
# print(maskify('uulib'))

# https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python


def separate(x):
    r = [x % 10]
    while x > 10:
        x = int(x / 10)
        r.insert(0, x % 10)
    return r


def power_sumDigTerm(n):
    res = []
    numb = 456
    list_numb = separate(numb)
    print(list_numb)
    while n >= len(res):
        if sum(list_numb) ** len(list_numb) == numb:
            res.append(numb)
            print(res)
        if len(res) == n:
            return res[-1]
        numb += 1


print(power_sumDigTerm(3))
