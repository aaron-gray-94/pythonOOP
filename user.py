class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username# and we use the values passed in to set the name attribute
        self.email = email_address# and the email attribute
        self.account = BankAccount(int_rate=0.02, balance=0)# the account balance is set to $0, so no need for a third parameter
    def make_deposit(self, amount):# takes an argument that is the amount of the deposit
        self.account_balance += amount# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount# the specific user's account decreases by the amount of the value received
        return self
    def display_user_balance(self):
        print("User: ", self.name + "  Account Balance: ", self.account_balance)# the account balance prints
        return self
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
        print(self.account.balance)		# or access its attributes

guido = User("Guido van Rossum", "guido@python.com")
guido.make_deposit(500)
guido.make_withdrawal(350)
guido.display_user_balance()	# output: Guido van Rossum


guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawal(50)
guido.display_user_balance()

monty = User("Monty Python", "monty@python.com")
monty.make_deposit(200)
monty.make_deposit(200)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
monty.display_user_balance()

jayne = User("Jayne Doe", "jayne@python.com")
jayne.make_deposit(1000)
jayne.make_withdrawal(300)
jayne.make_withdrawal(300)
jayne.make_withdrawal(300)
jayne.display_user_balance()

guido.transfer_money(jayne, 50)