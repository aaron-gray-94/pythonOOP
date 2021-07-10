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

class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username# and we use the values passed in to set the name attribute
        self.email = email_address# and the email attribute
        self.account = BankAccount(int_rate=0.02, balance=0)# the account balance is set to $0, so no need for a third parameter
    def make_deposit(self, amount):# takes an argument that is the amount of the deposit
        self.account.deposit(amount)# the specific user's account increases by the amount of the value received
        return self.account
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)# the specific user's account decreases by the amount of the value received
        return self.account
    def display_user_balance(self):
        print("User: ", self.name + "  Account Balance: ", self.account)# the account balance prints
        return self.account
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        self.account.deposit(amount)
        return self.account
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
        print(self.account.balance)		# or access its attributes