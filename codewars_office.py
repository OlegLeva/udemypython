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

def get_count(input_str):
    num_vowels = 0
    for i in input_str:
        if i in 'aeiou':
            num_vowels += 1

    return num_vowels