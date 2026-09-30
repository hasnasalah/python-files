number1=float(input("Please enter a number?"))
number2=float(input("please enter another number?"))
choice=input("choose from the following options \n 1:Addition \n 2:subtraction \n 3:multiplication \n 4:division ")
if number1.isdigit() and number2.isdigit():

    number1 = float(number1)
    number2 = float(number2)

    if choice == "1":
        print(number1 + number2)

    elif choice == "2":
        print(number1 - number2)

    elif choice == "3":
        print(number1 * number2)

    elif choice == "4":
        if number2 == 0:
            print("We cannot divide by 0")
        else:
            print(number1 / number2)

    else:
        print("We don't have that option")

else:
    print("This is not a number. Please enter a valid number.")
