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

class CheckAccount(Account):

    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self,filepath)

    def transfer(self, amount):
        self.balance -=( amount + self.fee)
        self.commit()

checkAccount = CheckAccount('balance.txt', 1)
# checkAccount.deposit(100)
checkAccount.transfer(110)
print(checkAccount.balance) # we defined balance as a instance variable / property of the class
