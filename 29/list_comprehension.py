greetings = ['hello', 'hi', 'hey', 'hola']
letters = []
for word in  greetings:
    letters.append(word[1])
print(letters)

letters1 = [word_2[1] for word_2 in greetings]
print(letters1)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digits_odd = []
for d in digits:
    if d % 2 != 0:
        digits_odd.append(d)
print(digits_odd)

digits_odd_1 = [i for i in digits if i % 2 != 0]
print(digits_odd_1)
