import math, random,platform

number=random.randint(1,100)

square_number=math.floor((math.sqrt(number)))
print(f"Random number: {number}")
print(f"Square Root (floored): {square_number}")
print(f"Operating System: {platform.system()}")
print(f"Python Version: {platform.python_version()}")