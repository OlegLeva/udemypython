def is_cat_here(*args):
    list_1 = []
    for i in args:
        list_1.append(i.lower())
    if 'cat' in list_1:
        return True
    else:
        return False

print(is_cat_here('go', 'Cat'))

def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False

print(is_item_here(2, 4, 6, 2, 3))


def your_favorite_color(my_color, **kwargs):
    if 'color' not in kwargs:
        print(f'My favorite color is {my_color}, what is your favorite color?')
    if 'color' in kwargs:
        print(f'My favorite color is {my_color}, but {kwargs["color"]} is also pretty good!')


your_favorite_color('green', color='blue', season='summer')