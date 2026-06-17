from datetime import datetime

class BankAccount:
    def __init__(self, owner, account_number, initial_balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = initial_balance
        self.transaction_history = []
        self._add_transaction('OPEN', initial_balance)

    def _add_transaction(self, transaction_type, amount):
        self.transaction_history.append({
            'transaction_type': transaction_type,
            'amount': amount,
            'balance_after': self._balance,
            'timestamp': datetime.now().strftime('%d-%m-%Y - %H:%M')
        })    

    def __str__(self):
        return f'{self.owner}, your account number is: {self.account_number} and your balance is: {self.balance}.'

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

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self.balance = self.balance + amount
        self._add_transaction(
            'DEPOSIT', amount
        )
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        elif amount > self.balance:
            raise ValueError
        else:
            self.balance = self.balance - amount
            self._add_transaction(
                'WITHDRAW', amount
            )

    def show_history(self):
        for item in self.transaction_history:
            print(f'Transaction type: {item["transaction_type"]}, amount: {item["amount"]}, balance after: {item["balance_after"]}, time: {item["timestamp"]}')

class SavingsAccount(BankAccount):
    def __init__(self, owner, account_number, interest_rate, initial_balance=0):
        super().__init__(owner, account_number, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = self.balance + interest
        self._add_transaction(
            'DEPOSIT_INTEREST', interest
        )

class BusinessAccount(BankAccount):
    def __init__(self, owner, account_number, company_name, initial_balance=0):
        super().__init__(owner, account_number, initial_balance)
        self.company_name = company_name

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError
        elif amount > 10000:
            raise ValueError
        elif amount > self.balance:
            raise ValueError
        else:
            self.balance = self.balance - amount
            self._add_transaction(
                'BUSINESS_WITHDRAW', amount
            )

    def pay_invoice(self, amount, description):
        if amount <= 0:
            raise ValueError
        elif amount > self.balance:
            raise ValueError
        else:
            self.balance = self.balance - amount
            self._add_transaction(
                'INVOICE', amount
            )
            print(f'The invoice for {description} has been paid.')

account1 = BankAccount('James', 'NL123456789', 500)
account1.deposit(250)
account1.withdraw(500)
account1.show_history()

account2 = SavingsAccount('Frederik', 'ES928387023984', 0.015, 2500)
account2.add_interest()
account2.deposit(5000)
account2.withdraw(100)
account2.show_history()

account3 = BusinessAccount('Jill', 'USA298437523984723', 'Microsoft', 15000)
account3.deposit(8000)
account3.withdraw(1500)
account3.pay_invoice(3000, 'Phone bill')
account3.show_history()