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

oleg_L = User('oleh', 'levytskyi', '+380509001818', 0)

print(oleg_L.describe_user())
print(oleg_L.greet_user())
oleg_L.increment_login_attempts()
oleg_L.increment_login_attempts()
print(oleg_L.login_attempts)
oleg_L.reset_login_attempts()
print(oleg_L.login_attempts)