#Day26:Raise an exception if a user tries to withdraw more money than is available in their account
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Withdrawal failed: Tried to withdraw {amount}, but balance is only {balance}."
        super().__init__(message)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawal successful! New balance: {self.balance}")
try:
    account = BankAccount("Alice", 1000)
    withdraw_amount = float(input("Enter amount to withdraw: "))
    account.withdraw(withdraw_amount)
except InsufficientFundsError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a number.")
