def eigth_queens(n, m):
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

    for row in a:
        print(' '.join([str(elem) for elem in row]))

eigth_queens(0, 0, 8)
