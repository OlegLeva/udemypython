def move(n, m, a):
    for i in range(8):
        for j in range(8):
            if i == n and j == m:
                a[i][j] = 'Q'
            elif i != n and j == m:
                a[i][j] = '*'
            elif i == n and j != m:
                a[i][j] = '*'
            elif abs(i - n) == abs(j - m):
                a[i][j] = '*'


def queen_move(numb, lett):
    numeral_dict = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
    letters_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    n = numeral_dict[numb]
    m = letters_dict[lett]
    a = [['.'] * 8 for _ in range(8)]
    move(n, m, a)
    count = 1

    for i in a:
        for j in i:
            if j == '.':
                move(a.index(i), i.index(j), a)
                count += 1
    if count != 8:
        pass ####


    for row in a:
        print(' '.join([str(elem) for elem in row]))
    print(count)

queen_move(1, 'f')