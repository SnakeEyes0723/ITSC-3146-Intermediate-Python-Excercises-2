#For this part of the assignment, I had to look up how to create constructors in Python, which I learned how to do here: https://www.geeksforgeeks.org/constructors-in-python/

class BankAccount():
    def _init_(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, money: int):
        self.balance = self.balance + money

    def withdraw(self, money: int):
        self.balance = self.balance - money

    def get_balance(self):
        return self.account_name + " has a balance of " + str(self.balance)