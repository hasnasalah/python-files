#in this program we will loop through numbers from 1 to 50 and sum all even numbers
sum=0
for i in range(1,51):
    if i%2==0:
        sum+=i

print(f"The sum of even numbers from 1 to 50 is: {sum}")