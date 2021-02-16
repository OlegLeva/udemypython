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

#
# def separate(x):
#     r = [x % 10]
#     while x > 10:
#         x = int(x / 10)
#         r.insert(0, x % 10)
#     return r
#
#
# def power_sumDigTerm(n):
#     res = []
#     numb = 81
#     while n > len(res):
#         list_numb = separate(numb)
#         sum_list = sum(list_numb)
#         if sum_list ** len(list_numb) == numb:
#             res.append(numb)
#         numb += 1
#     return res[-1]
#
#
#
# print(power_sumDigTerm(4))
#
#
# def power_sumDigTerm(n):
#     power_sum = []
#     for i in range(2, 100):
#         for j in range(2, 50):
#             pow_i = i ** j
#             if sum(map(int, str(pow_i))) == i:
#                 power_sum.append(pow_i)
#     power_sum.sort()
#     return power_sum[n-1]
#
# print(power_sumDigTerm(30))

# def likes(names):
#     if len(names) == 0:
#         return 'no one likes this'
#     if len(names) == 1:
#         return f'{names[0]} likes this'
#     if len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     if len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     if len(names) > 3:
#         return f'{names[0]}, {names[1]} and {len(names)-2} others like this'
#
# def printer_error(s):
#     alfa = 'abcdefghijklmnopqrstuvwxyz'
#     error = 0
#     for a in s:
#         if a not in alfa[:13]:
#             error += 1
#     return f'{error}/{len(s)}'
#
# def sort_array(source_array):
#     odd_list = []
#     for n in source_array:
#         if n % 2 != 0:
#             odd_list.append(n)
#     a = list(map(lambda x: 'c' if x % 2 != 0 else x, source_array))
#     odd_list.sort()
#     i = 0
#     j = 0
#     while i < len(a):
#         if a[i] == 'c':
#             a[i] = odd_list[j]
#             j += 1
#         i += 1
#     return a
#
# print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

#
# alfa = 'abcdefghijklmnopqrstuvwxyz'
# a=[1,2,3,4,5,6,7,8,9,10]
# a = list(map(lambda x: 'c' if x % 2 != 0 else x, a))
# print(a)
# even = [1,3,5,7,9]
# j = 0
# i = 0
# while i < len(a):
#     if a[i] == 'c':
#         a[i] = even[j]
#         j += 1
#     i += 1
# print(a)

# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
#
# def find_reverse_number(n):
#     res = [0]
#     for n1 in range(-1, 1000001):
#         n11 = n1
#         n2 = 0
#         while n11 > 0:
#             digit = n11 % 10
#             n11 = n11 // 10
#             n2 = n2 * 10
#             n2 = n2 + digit
#             if n2 == n1:
#                 res.append(n1)
#     # print(res)
#     return res[n-1]
#
# print(find_reverse_number(100))

#
#
# def find_reverse_number(n):
#     res = [0]
#     n1 = 1
#     while len(res) < n:
#         if n1 == int((str(n1))[::-1]):
#             res.append(n1)
#         n1 += 1
#     return res[n-1]
#
# print(find_reverse_number(100))

# def evens_and_odds(n):
#     if n % 2 == 0:
#         return (bin(n))[2:]
#     if n % 2 != 0:
#         return (hex(n))[2:]
#
# print(evens_and_odds(13))
#
# def sum_of_minimums(numbers):
#     res = 0
#     for i in numbers:
#         res += min(i)
#     return res
#
# print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))
#
# def sum_of_minimums(numbers):
#     res = 0
#     return [min(i) for i in numbers]
#
# print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))

# def fake_bin(x):
#     y = ''
#     for i in x:
#         if int(i) < 5:
#             y += '0'
#         if int(i) >= 5:
#             y += '1'
#     return y
#
# print(fake_bin("366058562030849490134388085"))

# def summy(string_of_ints):
#     sum_of_ints = sum(map(int, string_of_ints.split()))
#
#     return sum_of_ints
#
# print(summy('55 3 5'))
#
# def comp(array1, array2):
#     if sorted([x*x for x in array1]) == sorted(array2):
#         return True
#     else:
#         return False
#
#
#
#
#
#
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 1464, 20736, 361, 25921, 361, 20736, 361]
# print(comp(a, b))

# alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(set('abcdef') - set('abcdf'))

# def find_missing_letter(chars):
#     chars.sort()
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     index_start = alphabet.index(chars[0])
#     index_end = alphabet.index(chars[-1])
#     chars_1 = alphabet[index_start: index_end + 1]
#     return (set(chars_1) - set(chars)).pop()
#
# print(find_missing_letter(["O","Q","R","S"]))
#
# def check_empty_list(l):
#     for i in l:
#         if i == []:
#             l.remove(i)
#     return l
#
# def snail(snail_map):
#     res = []
#
#     while snail_map:
#         while snail_map[0]:
#             res.append((snail_map[0].pop(0)))
#         check_empty_list(snail_map)
#         if not snail_map:
#             break
#
#         for i in snail_map:
#             res.append(i.pop(-1))
#         check_empty_list(snail_map)
#         if not snail_map:
#             break
#
#         while snail_map[-1]:
#             res.append((snail_map[-1].pop(-1)))
#         check_empty_list(snail_map)
#         if not snail_map:
#             break
#
#         for i in snail_map[::-1]:
#             print(i)
#             res.append(i.pop(0))
#         check_empty_list(snail_map)
#         if not snail_map:
#             break
#
#
#     return res
#
#
# print(snail([[1,2,3,4,5,6],
#              [20,21,22,23,24,7],
#              [19,32,33,34,25,8],
#              [18,31,36,35,26,9],
#              [17,30,29,28,27,10],
#              [16,15,14,13,12,11]]))
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
#
# def digital_root(n):
#     while n >= 10:
#         n = sum(map(int, (str(n))))
#         print(n)
#     return n
#
#
#
#
# print(digital_root(132189))
#   -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6

# def persistence(n):
#     while n >= 10:
#         n = eval('*'.join(str(n)))
#     return n
#
# print(persistence(25))

# def points(games):
#     count = 0
#     for i in games:
#         if i[0] > i[2]:
#             count += 3
#         if i[0] == i[2]:
#             count += 1
#     return count
#
# print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))

# def reverse_words(s):
#     return ' '.join((s.split())[::-1])
#
# print(reverse_words("The greatest victory is that which requires no battle"))
#
# def reverse_words(text):
#     res = []
#     for w in text.split():
#         x = w[::-1]
#         res.append(x)
#     return ' '.join(res)
#
#
# print(reverse_words("This is an example!"))

# def in_array(array1, array2):
#     res = []
#     for i in a1:
#         for j in a2:
#             if i in j and i not in res:
#                 res.append(i)
#     res.sort()
#     return res
#
#
#
# a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# print(in_array(a1, a2))

# def friend(x):
#     return [n for n in x if len(n) == 4]
#
# print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))

# def find_short(s):
#     return min([len(x) for x in s.split()])
# print(find_short("lets talk about javascript the best language"))

# def prefill(n, v='undefined'):
#     l = []
#     if n == 0:
#         return []
#     if type(n) != int:
#         raise TypeError('{} is invalid'.format(n))
#     else:
#         l.append(v)
#         return l*n
#
# print(prefill('xyz', prefill(3, 'aa')))

def tower_builder(n_floors):
    res = []
    z = "*"
    size = n_floors*2-1
    count = 1
    while count <= n_floors:
        s = "{:^"f"{size}""}".format(z)
        res.append(s)
        z += "**"
        count += 1
    return res



print(tower_builder(6))