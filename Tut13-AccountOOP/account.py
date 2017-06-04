class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount
        self.commit()

    def deposit(self, amount):
        self.balance += amount
        self.commit()

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


account = Account('balance.txt') #this makes an instancce of the Account class

print(account.balance)
account.withdraw(50)
print(account.balance)
account.deposit(100)
print(account.balance)
