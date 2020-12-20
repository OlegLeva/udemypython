my_list = [
   [1, 5], #отсортировать
   [1, 6],
   [16, 19],
   [5, 11]
]
new_list = []

var = my_list[0][0] <= my_list[1][0] <= my_list[0][1] or \
      my_list[1][0] <= my_list[0][1] <= my_list[1][1]

cand = []
cand = sort_my_list
# def sum_of_intervals(intervals):
#     l = []
#     for s, e in intervals:
#         l += range(s, e)
#
#     return len(set(l))
#
# sum_of_intervals(my_list)