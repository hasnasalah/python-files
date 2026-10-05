# in this function we will print bacj the greeting 
def greet_user(name):
    if name=="":
        print("Hello, Welcome")
    else: 
        print(f"Hello, {name}! Welcome!")

#  this function is a sum of two numbers
def add_two_numbers(a, b):
    return a+b

# this function will check if a number is even or no
def is_even(num):
    if num%2==0:
        return True
    else: return False
    
    
# printing results
greet_user("hasna")
greet_user("")

print(add_two_numbers(5,6))
print(add_two_numbers(0,1))

print("3 is even: ",is_even(3))
print("4 is even: ",is_even(4))
