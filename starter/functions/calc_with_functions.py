
# conversion and the division operation at minimum.
#addition function
def add(a,b):
    return a+b

#subtraction function
def subtraction(a,b):
    return a-b

#multiplication function
def multiplication(a,b):
    return a*b

# divition function
def division(a,b):
    return a/b

# calculate function 

def calculate(a,b,op):
    if op=="+":
        print(add(a,b))
    elif op=="-":
        print(subtraction(a,b))
    elif op=="*":
        print(multiplication(a,b))
    else:
        try:
            print("Result:", division(a,b))
        except ZeroDivisionError:
            print("You cannot divide by zero.")
try:
    a=int(input("enter a number: "))
    b=int(input("Enter another number: "))
    ob=input("please enter the operation symbole (/,+,*,-): ")
    calculate(a,b,ob)
except ValueError:
    print("Please enter numbers only.")
  
    
     
    

