class BlogPost:

    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


post1 = BlogPost(user_name='Oleg', text='Hi', number_of_likes=7)
post2 = BlogPost(user_name='Nik', text='Hello', number_of_likes=5)
post3 = BlogPost('Olga', 'bla bla bla', 11)

post2.number_of_likes = 99
post3.number_of_likes = 999

print(post1.number_of_likes)
print(post2.number_of_likes)
print(post3.number_of_likes)
