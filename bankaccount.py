class BankAccount:
    def __init__(self, int_rate=.05, balance=0): # don't forget to add some default values 
        self.interest = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount# the specific user's account increases by the amount of the value received
        return self
    def withdraw(self, amount):
        self.balance -= amount# the specific user's account decreases by the amount of the value received
        return self
    def display_account_info(self):
        print("Interest: ", self.interest, "  Account Balance: ", self.balance)# the account balance prints
        return self
    def yield_interest(self):
        self.balance = (self.interest+1)*self.balance
        return self


guidoAccount = BankAccount()
montyAccount = BankAccount()

guidoAccount.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

montyAccount.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()