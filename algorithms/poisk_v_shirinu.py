from collections import deque

my_famyly_dict = {}
my_famyly_dict['oleg'] = ['olga', 'nikita', 'ivan', 'andrey', 'sasha', 'tanya']
my_famyly_dict['olga'] = ['oleg', 'nikita', 'ivan', 'galina', 'dmitriy']
my_famyly_dict['nikita'] = []
my_famyly_dict['ivan'] = []
my_famyly_dict['andrey'] = ['masha_l', 'dasha', 'sasha', 'tanya']
my_famyly_dict['masha_l'] = []
my_famyly_dict['dasha'] = []
my_famyly_dict['sasha'] = ['oleg', 'andrey', 'tanya']
my_famyly_dict['tanya'] = ['oleg', 'andrey', 'sasha']
my_famyly_dict['galina'] = ['olga', 'dmitriy']
my_famyly_dict['dmitriy'] = ['olga', 'galina']

def search_seller(name):
    deque_name = deque()
    deque_name += my_famyly_dict[name]
    searched = []
    while deque_name:
        person = deque_name.popleft()
        if person not in searched:
            if who_is_composer(person):
                return person.title() + ' composer.'
            else:
                deque_name += my_famyly_dict[person]
                searched.append(person)
    return False


def who_is_composer(person):
    if person[-3:] == 'sha':
        return person

print(search_seller('oleg'))
