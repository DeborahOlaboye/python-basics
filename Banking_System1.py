class Account:
    def __init__(self, account_number, account_name, balance = 0.0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Name: {self.account_name}\nBalance: {self.Account_balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Your account {account_number} has been credited with {amount} from {self.account_name}. New balance is {self.Account_balance}.")
        else:
            print("Deposit amount cannot be negative")

    def withdraw(self, amount):
        if amount > 0:
            if self.Account_balance >= 0:
                self.Account_balance -= amount
            print(f"Your account {account_number} has been debited with {amount} to {self.account_name}. New balance is {self.Account_balance}.")
        else:
            print("Insufficient Balance")

    def transfer(self, amount, beneficiary_account):
        if amount > 0:
            if self.Account_balance >= amount:
            self.Account_balance -= amount
            beneficiary_account.deposit(amount)
            print(f"Transfer of {amount} successful")
        else:
            print("Insufficient funds")


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_name, initial_balance=0.0):
        account = Account(account_number, account_name, initial_balance)
        self.accounts.append(account)
        print("Account created")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def deposit_to_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw_from_account(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer_between_accounts(self, from_account_number, to_account_number, amount):
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)
        if from_account and to_account:
            from_account.transfer(amount, to_account)
        else:
            print("One or both accounts not found.")

    def view_all_accounts(self):
        for account in self.accounts:
            print(account)


# User Interface
bank = Bank()

while True:
    print("\n===== Bank Menu =====")
    print("1. Create a new account")
    print("2. Deposit to an account")
    print("3. Withdraw from an account")
    print("4. Transfer between accounts")
    print("5. View all accounts")
    print("6. Find an account by account number")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        bank.create_account(account_number, account_holder)

    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        bank.deposit_to_account(account_number, amount)

    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        bank.withdraw_from_account(account_number, amount)

    elif choice == "4":
        from_account_number = input("Enter sender's account number: ")
        to_account_number = input("Enter recipient's account number: ")
        amount = float(input("Enter amount to transfer: "))
        bank.transfer_between_accounts(from_account_number, to_account_number, amount)

    elif choice == "5":
        print("\n===== All Accounts =====")
        bank.view_all_accounts()

    elif choice == "6":
        account_number = input("Enter account number: ")
        account = bank.find_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please choose again.")
#Get balance
@property
def balance(self):
    return self.balance

#Set balance
@balance.setter
def balance(self, new_balance):
    self.balance = new_balance


