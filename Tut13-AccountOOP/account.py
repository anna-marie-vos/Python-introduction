class Account:
    """the Account class has
    withdraw (amount)
    deposit (amount)
    commit() which saves it to the txt file
    """

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
    """this class has a transfer method that uses the amount as an input"""

    type ="check account" # this is an attribute

    def __init__(self, filepath, fee): #this is a constructor
        self.fee = fee
        Account.__init__(self,filepath)

    def transfer(self, amount): # this is a method
        self.balance -=( amount + self.fee)
        self.commit()

JacksAccount = CheckAccount('jack.txt', 1)
# checkAccount.deposit(100)
JacksAccount.transfer(60)
print(JacksAccount.balance) # we defined balance as a instance variable / property of the class

JohnsAccount = CheckAccount('john.txt', 1)
# checkAccount.deposit(100)
JohnsAccount.transfer(50)
print(JohnsAccount.balance)
print(JohnsAccount.__doc__)
