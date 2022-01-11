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

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.interest_rate
        return self


    @classmethod
    def printAllAccounts(cls):
        for account in cls.accounts_list:
            account.display_account_info()

checking_account = BankAccount(0.01)
saving_account = BankAccount(0.05)

checking_account.deposit(100).deposit(150).deposit(250).withdraw(123).yield_interest().display_account_info()
saving_account.deposit(200).deposit(50).withdraw(100).withdraw(20).withdraw(75).withdraw(256).yield_interest().display_account_info()

print("NINJA BONUS:")
BankAccount.printAllAccounts()