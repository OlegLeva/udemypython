# pig_it('Hello world !')     # elloHay orldway !
import string


def pig_it(words):
    new_string = ''
    for word in words.split():
        if word in string.punctuation:
            new_string += word + ' '
        else:
            if word[-1] in string.punctuation:
                new_word = word[1:-1] + word[0] + "ay" + word[-1] + ' '
                new_string += new_word
            else:
                new_word = word[1::] + word[0] + "ay" + ' '
                new_string += new_word
    return new_string[:-1]


print(pig_it('Hello, world ! erny, T rn'))

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/python