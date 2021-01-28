class User:
    def __init__(self, first_name, last_name, phone, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.login_attempts = login_attempts

    def describe_user(self):
        return f'{self.first_name.title()} {self.last_name.title()}\nphone. {self.phone}'

    def greet_user(self):
        return f'Hello {self.first_name.title()} {self.last_name.title()}'

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self, privileges=''):
        self.privileges = privileges

    def show_privileges(self):
        self.privileges = [
            'Allowed advertising messages',
            'Allowed to delete users',
            'Allowed to ban users'
        ]
        for priveleg in self.privileges:
            print(priveleg)


class Admin(User):
    def __init__(self, first_name, last_name, phone, login_attempts):
        self.privileges = Privileges()
        super().__init__(first_name, last_name, phone, login_attempts)


oleg_L = User('oleh', 'levytskyi', '+380509001818', 0)

olga_L = Admin('olha', 'levytskayi', '+380507093655', 0)

nikita = Admin('nikita', 'levitskiy', '+380507093682', 0)

nikita.privileges.show_privileges()
print(nikita.describe_user())
