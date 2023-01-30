import BankAccount

name = "Jake's Account"
balance = 135.50

my_account = BankAccount.BankAccount()
my_account._init_("Jake's Account", balance)
my_account.deposit(51.30)
my_account.withdraw(42.71)
print(my_account.get_balance())