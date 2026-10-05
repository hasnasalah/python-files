# A function safe_divide(a, b) that returns the result of a / b if b is not zero. 
# If b is zero, the function should raise a ValueError with a message like “Cannot divide by zero”.

def safe_divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
  
  
## Demonstrate catching a generic exception  
try:
    print(safe_divide(5,0))
except ValueError as error:
    print(f"Error: {error}")
finally:
    print("division completed")
    
try:
    print(safe_divide(10,2))
except ValueError as error:
    print(f"Error: {error}")
finally:
    print("division completed")