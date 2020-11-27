def get_week_day():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    for day in week:
        yield day

    # index = 0
    # while True:
    #     if index >= len(week):
    #         index = 0
    #     yield week[index]
    #     index += 1


current_day = get_week_day()
while True:
    try:
        print(current_day.__next__())
        print(current_day.__next__())
        print(current_day.__next__())
        print(current_day.__next__())
        print(current_day.__next__())
        print(current_day.__next__())
        print(current_day.__next__())
        print(current_day.__next__())

    except StopIteration:
        break


def even_odd():
    even_odd_list = ['even', 'odd']
    index = 0
    while True:
        if index >= len(even_odd_list):
            index = 0
        yield even_odd_list[index]
        index += 1


even_odd_generator = even_odd()

print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))