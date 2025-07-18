#Day23:User defined Exception
#1]check Age
'''class CheckAge(Exception):
    def __init__(self, age):
        self.age = age
        self.message = "Age is below 18. You cannot vote."
        super().__init__(self.message)

try:
    age = int(input("Enter Age: "))
    if age < 18:
        raise CheckAge(age)
    else:
        print("You are eligible to vote.")
except CheckAge as e:
    print(e)'''

#2]Bank Withdrawal System

class InsufficientFundsException(Exception):
    def __init__(self, message="Withdrawal amount exceeds available balance!"):
        self.message = message
        super().__init__(self.message)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(
                f"Requested: {amount}, Available: {self.balance}"
            )
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

try:
    initial_balance = float(input("Enter your account balance: "))
    account = BankAccount(initial_balance)

    amount_to_withdraw = float(input("Enter amount to withdraw: "))
    account.withdraw(amount_to_withdraw)

except InsufficientFundsException as e:
    print("InsufficientFundsException:", e)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
