from functools import wraps


# def print_args(func):
#     @wraps(func)
#     def wraper(*args, **kwargs):
#         print(args)
#         print(kwargs)
#         print(func(*args, **kwargs))
#
#     return wraper
#
#
# @print_args
# def create_list_and_dict(*args, **kwargs):
#     list_1 = []
#     dict_1 = {}
#     for item in args:
#         list_1.append(item)
#     for key, value in kwargs.items():
#         dict_1[key] = value
#     return list_1, dict_1
#
#
# create_list_and_dict(1, 5, 8, 'W', car='toyota', model='Rav4')
#
#
# def hello_from_decorator(func):
#     @wraps(func)
#     def wrapper(*args):
#         print(func(*args) + " Hello from decorator!")
#     return wrapper
#
#
# @ hello_from_decorator
# def hello(name):
#     return name + ','
#
# hello('Oleg')


# def prohibit_more_than_2_args(function):
#     @wraps(function)
#     def wrappers(*args):
#         if len(args) > 2:
#             raise ValueError("Function must have less than 3 arguments!")
#         return function(*args) + " Rescue Rangers!"
#     return wrappers
#
#
# @prohibit_more_than_2_args
# def rescuer(*args):
#     list_name = " and ".join(args)
#     return list_name
#
# print(rescuer('Chip', 'Dale'))
# print(rescuer('Chip', 'Dale', 'Rocky'))
from time import sleep


def wait(n):
    def sleep_n(func):
        @wraps(func)
        def wrapper():
            sleep(n)
            print(f"There was a pause {n} seconds before execution {func.__name__}")
            return f"{func()} за {n} секунды"
        return wrapper
    return sleep_n


@wait(3)
def sleep_time():
    return 'Всё, выспался'


print(sleep_time())