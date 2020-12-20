class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name,
        self.text = text,
        self.number_of_likes = number_of_likes

person_1 = BlogPost('Oleg', 'Hello', 44)
person_2 = BlogPost('Olga', 'Big Hello', 33)
person_1.number_of_likes = 55
print(person_1.number_of_likes)
print(person_2.number_of_likes)
