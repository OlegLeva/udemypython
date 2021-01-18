# def divisors(integer):
#     res = []
#     for x in range(2, integer + 1):
#         if x == integer:
#             continue
#         if integer % x == 0:
#             res.append(x)
#     if res == []:
#         return f"{integer} is prime"
#     else:
#         return res
#
# print(divisors(13))
#
# def unique_in_order(iterable):
#     res = []
#     i = 1
#     if iterable == '' or []:
#         return []
#     else:
#         res.append(iterable[0])
#         while i < len(iterable):
#             if iterable[i] == res[-1]:
#                 i += 1
#                 continue
#             else:
#                 res.append(iterable[i])
#                 i += 1
#         return res
#
# print(unique_in_order(''))

# def tickets(people):
#     bill_list = []
#     for bill in people:
#         if bill == 25:
#             bill_list.append(25)
#             print(f'25 {bill_list}')
#         if bill == 50 and 25 in bill_list:
#             bill_list.append(50)
#             bill_list.remove(25)
#             print(f'50 {bill_list}')
#         if bill == 100 and bill_list.count(25) > 3:
#             bill_list.append(100)
#             bill_list.remove(25)
#             bill_list.remove(25)
#             bill_list.remove(25)
#             print(f'100/1 {bill_list}')
#         elif bill == 100 and 25 in bill_list and 50 in bill_list:
#             bill_list.append(100)
#             bill_list.remove(25)
#             bill_list.remove(50)
#             print(f'100/2 {bill_list}')
#     if len(people)*25 == sum(bill_list):
#         return "YES"
#     else:
#         return "NO"
#
# print(tickets([25, 50, 25, 100]))

# def nb_year(p0, percent, aug, p):
#     year = 0
#     while p0 < p:
#         p0 = p0 + p0 * (percent/100) + aug
#         year += 1
#     return  year
#
# print(nb_year(1500000, 0.25, 1000, 2000000))
#https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
def binary_array_to_number(arr):
    arr1 = arr[::-1]
    i = 0
    result = []
    for x in arr1:
        if x == 1:
            result.append(2**i)
        i += 1
    return sum(result)


