class User:
    def __init__(self,name):
        self.name=name
        self.balance = 0

    def make_deposit(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
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

stephen.transfer_money(jane,10300)
stephen.display_user_balance()
jane.display_user_balance()

print("method chaining:")
john.make_withdrawal(100).make_deposit(12345).make_deposit(5123).display_user_balance()