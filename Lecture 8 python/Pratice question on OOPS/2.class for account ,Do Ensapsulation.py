# Create Account class with 2 attributes - balances & account no.
# Create methods for debits ,credits & printing the balance.

class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
# this is method created for debit and credit--
    def debit(self,amount):  
        self.balance -= amount
        print("rs.",amount,"was debited:")
        print("total amount = ",self.get_balance())   

    def credit(self,amount):  
        self.balance += amount
        print("rs.",amount,"was credited:")
        print("total amount = ",self.get_balance()) 
# this is for return 
    def get_balance(self):
        return self.balance

acc1 = account(10000,123456) 
print("balance:", acc1.balance,",account_no:",acc1.account_no)
acc1.debit(int(input("enter debit value:")))      
acc1.credit(int(input("enter credit value:")))   #this i wrote so we can directly enter value

        
