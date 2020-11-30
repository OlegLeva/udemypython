# def get_current_day():
#     week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#     i = 0
#     while True:
#         if i >= len(week):
#             i = 0
#         yield week[i]
#         i += 1
#
#
# amount_day = int(input('Введите количество дней '))
# current_day = get_current_day()
# count = 0
# while count != amount_day:
#     print(next(current_day))
#     count += 1


def get_infinite_square_generator():
    """
    :return:
    """
    i = 1
    while True:
        yield i ** 2
        i += 1


infinite_square_generator = get_infinite_square_generator()

print(next(infinite_square_generator))
print(next(infinite_square_generator))
print(next(infinite_square_generator))
print(next(infinite_square_generator))
