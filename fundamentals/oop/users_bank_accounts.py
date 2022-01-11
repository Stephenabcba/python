class BankAccount:
    accounts_list = []
    def __init__(self, interest_rate, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount.accounts_list.append(self)

    @staticmethod
    def checkWithdrawAmount(curBalance, amount):
        if curBalance > amount:
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if BankAccount.checkWithdrawAmount(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def getBalance(self):
        return self.balance

    def get_account_info(self):
        return f"Balance: ${self.balance}"

    def display_account_info(self):
        print( f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.interest_rate
        return self


    @classmethod
    def printAllAccounts(cls):
        for account in cls.accounts_list:
            account.display_account_info()

class User:
    def __init__(self,name):
        self.name=name
        self.account = BankAccount(0.02)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name} " + self.account.get_account_info())
        return self


class UserMultAcc:
    def __init__(self,name):
        self.name=name
        self.accounts = {
            "Checking": BankAccount(0.02),
            "Savings": BankAccount(0.05)
        }

    def make_deposit(self,amount, accountName):
        self.accounts[accountName].deposit(amount)
        return self

    def make_withdrawal(self,amount, accountName):
        self.accounts[accountName].withdraw(amount)
        return self

    def display_user_balance(self):
        account_list = self.accounts.items()
        for account in account_list:
            print(f"User: {self.name}, {account[0]} " + account[1].get_account_info())
        return self

stephen = User('Stephen')
john = User('John')
jane = User('Jane')

stephen.make_deposit(10412)
stephen.make_deposit(50123)
stephen.make_deposit(12345)
stephen.make_withdrawal(51230)
stephen.display_user_balance()

john.make_deposit(123456)
john.make_deposit(512352)
john.make_withdrawal(2131)
john.make_withdrawal(20)
john.display_user_balance()

jane.make_deposit(100)
jane.make_withdrawal(15)
jane.make_withdrawal(26)
jane.make_withdrawal(17)
jane.display_user_balance()

print("method chaining:")
john.make_withdrawal(100).make_deposit(12345).make_deposit(5123).display_user_balance()


print("SENSEI BONUS")
bob = UserMultAcc('Bob')
bob.make_deposit(123456, "Checking")
bob.make_deposit(512352, "Savings")
bob.make_withdrawal(2131, "Checking")
bob.display_user_balance()