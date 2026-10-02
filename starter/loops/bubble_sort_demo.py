numbers=[64, 25, 12, 22, 11]
for i in range(len(numbers)-1):
    print(numbers)
    if numbers[i]>numbers[i+1]:
        numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
print(numbers)