class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self, name):
        print(f'Hi, my name is {name}.')


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)

    def speak(self, name):
        print(f'Hi, my name is {name} and I will kill you')

    def kill(self, gamer):
        gamer.health = 0
        print('Bang-bang, now you\'re dead')

gamer1 = GameCharacter('Ol', 30, 5)
gamer2 = Villain("Nik", 44, 9)
print(gamer1.health)
gamer2.kill(gamer1)
print(gamer1.health)
print(gamer2.health)
gamer2.speak('Nik')
gamer1.speak('Ol')

