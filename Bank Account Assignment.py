class BankAccount:
    def __init__(self, account_name, account_number, account_balance, initial_balance = 0):
        self.account_name = account_name
        self.account_number = account_number
        self.initial_balance = account_balance

        def deposit(self, amount):
            if amount > 0:
                account_balance += amount
                print(f"Your account {account_number} has been credited with {amount} from {account_name}. New balance is {account_balance}. Transaction Date")
            else:
                print(f"Deposit amount cannot be negative")
        
        def withdraw(self, amount):
            if amount > 0:
                if account_balance >= amount:
                    account_balance -= amount
                    print(f"Your account {account_number} has been debited with {amount} to {account_name}. New balance is {account_balance}. Datw")
            else:
                print(f"Withdrawal amount cannot be Negative")

