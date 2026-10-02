numbers=[20,77,1,8,7]
 #print the list
print("Original list:")
for i in numbers:
    print(i)
# numbers=numbers.sorted()
nums=sorted(numbers)
#printing the list sorted
print("Sorted list:")
for i in nums:
    print(i)
# displying the numbers using sort()
print("list printed using sort:")
numbers.sort()
for i in numbers:
    print(i)
#add  a number to the list 
numbers.append(55)
# remove a number from the list``
numbers.remove(77)
#print the list before reverse 
print("list before reverse:")
print(numbers)
#reverse the list 
numbers.reverse()
# print the list
print("list reversed:")
print(numbers)
