class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, amount_add):
        self.balance += amount_add

    def withdraw(self, amount_withdraw):
        self.balance -= amount_withdraw

client1 = BankAccount(1, 'Oleg', 'Lev')
print(client1.balance)
client1.add(99)
print(client1.balance)
client1.withdraw(44.4)
print(client1.balance)


