from exceptions import InsufficientFundsError
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number=account_number
        self.owner=owner
        self.balance=balance
    
    def deposit(self, amount): 
        if amount<=0:
            raise ValueError("This is not a valid amount")
        else:
            self.balance+=amount
            print(f"the ${amount} was deposited succefully your balance now is: ${self.balance}")
            
    def withdraw(self, amount): 
        if  amount <= 0:
           raise ValueError("Withdrawal amount must be positive.")
        elif self.balance<amount:
            raise InsufficientFundsError(amount)
        else:
            self.balance-=amount
            print(f"you withrowed ${amount} successfully your balance now is ${self.balance}")
    
    def __str__(self):
        return (f"Account Number: {self.account_number}\n Account Owner: {self.owner}\n Balance: {self.balance}")
        
        
class Saving(BankAccount):
    def __init__(self,account_number,owner,balance,interest_rate):
        super().__init__(account_number,owner,balance)
        self.interest_rate=interest_rate
    
    def apply_interest(self): 
        self.balance+=self.balance*self.interest_rate/100
    
    def __str__(self):
        return super().__str__()+f"\n Interest Rate: {self.interest_rate}%"
        