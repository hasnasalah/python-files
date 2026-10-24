
try:
     a=1/0
except ArithmeticError:
    print("ar")
except ZeroDivisionError:
    print("ze")