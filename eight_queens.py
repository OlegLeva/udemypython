def count_queens(numb, lett):
    numeral_dict = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
    letters_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    n = 8
    ii = numeral_dict[numb]
    jj = letters_dict[lett]
    i = ii
    j = jj
    a = [[1] * n for _ in range(n)]
    a[i][j] = 0
    if a[i][j] == 0:
        a[i] = [c * 0 for c in range(0, n)]
        for l in range(0, n):
            a[l][j] = 0
        if i > j:
            i -= j
            j = 0
            while i < n:
                a[i][j] = 0
                i += 1
                j += 1
            i = ii
            j = jj
            j += i
            i = 0
            while j >= 0:
                a[i][j] = 0
                i += 1
                j -= 1
        if i <= j:
            j -= i
            i = 0
            while j < n:
                a[i][j] = 0
                i += 1
                j += 1
            i = ii
            j = jj
            i = i - (7 - j)
            j = 7
            while i < n:
                a[i][j] = 0
                i += 1
                j -= 1

    for row in a:
        print(' '.join([str(elem) for elem in row]))

print(count_queens(1, 'b'))