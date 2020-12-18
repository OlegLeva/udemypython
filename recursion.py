def privet(x):
    if x == 0:
        return 1
    else:
        print(x)
        return x * privet(x-1)

print(privet(5))

def fib(y):
    if y == 0:
        return 0
    if y == 1:
        return 1
    else:
        return (fib(y-1) + fib(y-2))

print(fib(40))
