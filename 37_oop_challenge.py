class Account():

    def __init__(self,owner,balance=0):

        self.owner=owner
        self.balance=balance

    def deposit(self,dep_amnt):

        self.balance=self.balance+dep_amnt
        print(f"Added {dep_amnt} to the balance")

    def withdrawl(self,wd_amnt):

        if self.balance >= wd_amnt:
            self.balance=self.balance-wd_amnt
            print("withdrawl accepted")
        else:
            print("Sorry not enough funds.")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

a = Account("Sam",500)
print(a)
a.deposit(400)
a.withdrawl(800)
a.withdrawl(150)