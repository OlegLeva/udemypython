def at_voice():
    print('Meow!')


def dog_voice():
    print('Woof!')


at_voice()
dog_voice()


def at_voice():
    return 'Meow!'


def dog_voice():
    return 'Woof!'


print(at_voice() * 2)
print(dog_voice() * 2)


def get_voice(voice):
    return voice + '!'

print(get_voice('Hello'))


def get_list(a, b):
    list_odd = []
    for i in range(a, b + 1):
        if i % 2 == 1:
            list_odd.append(i)
    return (list_odd)

print(get_list(1, 20))

def get_list(a, b):
    list_odd = [i for i in range(a, b + 1) if i % 2 == 1]
    return (list_odd)

print(get_list(1, 10))
