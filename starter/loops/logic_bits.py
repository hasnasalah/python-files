# Demonstrates the use of logical operators: for example, ask the user for two boolean inputs
# (True/False or 1/0) and show the results of and, or, 
# and not on those inputs.
a = bool(int(input("Enter 1 or 0: ")))
b = bool(int(input("Enter 1 or 0: ")))

print("AND:", a and b)
print("OR:", a or b)
print("NOT a:", not a)
print("NOT b:", not b)

# Demonstrates bitwise operators (&, |, ^, ~, <<, >>) 
# on two small integers (for example, 5 and 3).
# Print the results in binary form using bin() 
# to show what is happening at the bit level.
# This task is for exploration and wil
a = 5
b = 3
print("a in binary:", bin(a))
print("b in binary:", bin(b))
print("AND:", bin(a & b))
print("OR:", bin(a | b))
print("XOR:", bin(a ^ b))
print("NOT a:", bin(~a))
print("a << 1:", bin(a << 1))
print("a >> 1:", bin(a >> 1))