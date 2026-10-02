grade=int(input(" please enter your grade in the range of(0-100)"))
# we will display the result of the grades 
#90-100: A
#80-89: B
#70-79: C
#60-69: D
#0-59: F
if grade>=90 and grade <=100:
    print("your grade is: A")
elif grade >=80 and grade<=89:
    print("your grade is: B")
elif grade >=70 and grade <=79:
    print("your grade is: C")
elif grade >=60 and grade <=69:
    print("your grade is: D")
elif grade >=0 and grade <=59:
    print("your grade is: F")


if grade<=100 and grade >=79:
    print("congratulation")
else:
    print("try your best next quarter")
    