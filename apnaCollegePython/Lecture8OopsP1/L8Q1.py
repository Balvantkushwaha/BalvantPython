class Account:
    def __init__(self, bal,acc):
        self.balance = bal
        self.account_no = acc
        # debit 
    def debit(self,ammount):
        self.balance -= ammount
        print("Rs.",ammount," was debited")
        print("total balance",self.get_balance())
        # cradit 
    def cradit(self, ammount):
        self.balance +=ammount
        print("Rs.",ammount,"was Cradited",self.get_balance())
        print("total balance",self.get_balance())
        
    def get_balance(self):
        return self.balance
acc1 = Account(10000,12345)
print(acc1.get_balance())
acc1.cradit(500)
