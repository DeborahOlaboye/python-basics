
class BankAccount:
    def __init__(self, account_number, account_name, Account_balance = 0.0):
        self.account_number = account_number
        self.account_name = account_name
        self.Account_balance = Account_balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Name: {self.account_name}\nBalance: {self.Account_balance}"

#Function for deposits
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your account {self.account_number} has been credited with {amount} from {self.account_name}. New balance is {self.Account_balance}.")
        else:
            print("Deposit amount cannot be negative")
#Function for withdrawal
    def withdraw(self, amount):
        if amount > 0:
            if self.Account_balance >= 0:
                self.Account_balance -= amount
            print(f"Your account {self.account_number} has been debited with {amount} to {self.account_name}. New balance is {self.Account_balance}.")
        else:
            print("Insufficient Balance")
#Function for transfer
    def transfer(self, amount, beneficiary_account):
        if amount > 0:
            if self.Account_balance >= amount:
            self.Account_balance -= amount
            beneficiary_account.deposit(amount)
            print(f"Transfer of {amount} successful")
        else:
            print("Insufficient funds")

#Storing the bank information
class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_name, initial_balance=0.0):
        account = Account(account_number, account_name, initial_balance)
        self.accounts.append(account)
        print("Account created")