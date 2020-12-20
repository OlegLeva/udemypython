import time
start = time.time()
def sum_of_intervals(l):
    l.sort(key=lambda i: i[0])
    cand = l.pop(0)
    res = 0

    while l:
        interval = l.pop(0)
        x_0, y_0 = cand
        x_1, y_1 = interval
        if x_0 <= x_1 <= y_0 or x_1 <= y_0 <= y_1:
            cand = min(x_0, x_1), max(y_0, y_1)
        else:
            res += cand[1] - cand[0]
            cand = interval

    res += cand[1] - cand[0]

    return res


print(sum_of_intervals([[1, 2],[6, 10],[11, 15],[1, 5],[10, 20],[1, 6],[16, 19],[5, 11],[1, 2],[6, 10],
    [11, 15],[1, 5],[10, 20],[1, 6],[16, 19],[5, 11],[1, 2],[6, 10],[11, 15],[1, 5],[10, 20],[1, 6],[16, 19],
   [5, 11]]))

print(time.time()-start)