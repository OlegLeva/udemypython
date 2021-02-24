def queen_move(numb, lett):
    numeral_dict = {8: 0, 7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}
    letters_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    b = 8
    n = numeral_dict[numb]
    m = letters_dict[lett]
    a = [['.'] * b for _ in range(b)]
    for i in range(b):
        for j in range(b):
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

print(queen_move(5, 'f'))