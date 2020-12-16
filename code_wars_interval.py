def sum_intervals(l):
    l.sort(key=lambda i: i[0])
    cand = l.pop(0)
    res = 0

    while l:
        interval = l.pop(0)
        l[0][0], l[0][1] = cand
        l[1][0], l[1][1] = interval
        if l[0][0] <= l[1][0] <= l[0][1] or l[1][0] <= l[0][1] <= l[1][1]:
            cand = min(l[0][0], l[1][0]), max(l[0][1], l[1][1])
        else:
            res += cand[1] - cand[0]
            cand = interval

    res += cand[1] - cand[0]

    return res


print(sum_intervals([
    [1, 2],
    [6, 10],
    [11, 15]
]))