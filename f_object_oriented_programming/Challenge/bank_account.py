class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_balance):

        self.balance = self.balance + deposit_balance
        print(
            f"\nDeposit of ${deposit_balance} is successful.\nOwner:\t\t{self.owner}\nNew Balance:\t${self.balance}\n ")

    def withdraw(self, withdraw_balance):

        if withdraw_balance > self.balance:
            print(
                f"\nWithdrawl of ${withdraw_balance} is aborted.\nSorry ! Low Balance.\nOwner:\t\t{self.owner}\nBalance:\t${self.balance}\n ")
        else:
            self.balance = self.balance - withdraw_balance
            print(
                f"\nWithdrawl of ${withdraw_balance} is successful.\nOwner:\t\t{self.owner}\nNew Balance:\t${self.balance}\n ")

    def __str__(self):
        return f"\nOwner:\t\t{self.owner}\nBalance:\t${self.balance}"


accnt1 = Account("Deba", 90)
accnt1.deposit(300)
accnt1.withdraw(200)
accnt1.withdraw(200)
print(accnt1.owner)
print(accnt1.balance)
