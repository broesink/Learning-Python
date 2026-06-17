from datetime import datetime

class BankAccount:
    def __init__(self, owner, account_number, initial_balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = initial_balance
        self.transaction_history = []

    def __str__(self):
        return f'{self.owner}, your account number is: {self.account_number} and your balance is: {self._balance}.'

    #Property vs Setter
    #@property > What happens with account.balance
    #@balance.setter > what happens with account.balance = ...

    @property #property creates the door 'account.balance'
    def balance(self):
        return self._balance
    
    @balance.setter #the setter makes sure that when someone enters the property door, the followin code is used before changing the value
    def balance(self, balance):
        if balance < 0:
            raise ValueError("The balance can't be less than 0")
        self._balance = balance

    #def deposit(self, amount):
