# pig_it('Hello world !')     # elloHay orldway !
# import string
#
#
# def pig_it(words):
#     new_string = ''
#     for word in words.split():
#         if word in string.punctuation:
#             new_string += word + ' '
#         else:
#             if word[-1] in string.punctuation:
#                 new_word = word[1:-1] + word[0] + "ay" + word[-1] + ' '
#                 new_string += new_word
#             else:
#                 new_word = word[1::] + word[0] + "ay" + ' '
#                 new_string += new_word
#     return new_string[:-1]
#
#
# print(pig_it('Hello, world ! erny, T rn'))

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python


def sum_intervals(l):
    l.sort(key=lambda i: i[0])
    print(l, 'sort')
    cand = l.pop(0)
    print(l, '1 pop')
    print(cand, 'cant 1 pop')
    res = 0

    while l:
        interval = l.pop(0)
        print(l, '2 pop')
        l[0][0], l[0][1] = cand
        print(cand, 'cand')
        print(interval, ' 1 interval')
        l[1][0], l[1][1] = interval
        print(interval, '2 interval')
        if l[0][0] <= l[1][0] <= l[0][1] or l[1][0] <= l[0][1] <= l[1][1]:
            cand = min(l[0][0], l[1][0]), max(l[0][1], l[1][1])
        if l[0][1] < l[1][0]:
            print(l[0])
            res += cand[1] - cand[0]
            cand = interval

    res += cand[1] - cand[0]

    return res


print(sum_intervals([
    [1, 2],
    [6, 10],
    [11, 15]
]))
