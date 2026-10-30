from bank import BankAccount,Saving
from exceptions import InsufficientFundsError

#seed the bank account
bankAccount=BankAccount(145875,"Hasna",478)
print(bankAccount.__str__())
print("************************")
#deposit the account
bankAccount.deposit(150)


#withrow money sucess
bankAccount.withdraw(148)

#withrow unsucess

try:
    bankAccount.withdraw(2145865)
except InsufficientFundsError as e:
    print(e)
    
#deposit unsuccess

try:
    bankAccount.deposit(-100)
except ValueError as e:
    print(e)
    
print(bankAccount.__str__())


print("************************")
savingAccount=Saving(14587,"hala",140,25)
print(savingAccount.__str__())
print("************************")
savingAccount.deposit(100)
try:
    savingAccount.withdraw(5)
except InsufficientFundsError as e:
    print(e)
    
savingAccount.apply_interest()

print(savingAccount.__str__())
