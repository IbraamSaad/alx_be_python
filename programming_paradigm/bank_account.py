class BankAccount:
    def __init__(self, account_balance, intialized_balance = 0):
        self.account_balance = account_balance
        self.intialized_balance = intialized_balance
        self.account_balance += self.intialized_balance
    
    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        elif self.account_balance < amount:
            print("Insufficient funds.")
            return False
      

    def display_balance(self):
        print (f" Current Balance: ${self.account_balance}")

