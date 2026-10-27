# (a) Add a number: Prompt the user for an integer and append it to the list.
# (b) Remove a number: Prompt for an index and attempt to remove the element at that index using list.pop(index).
# (c) Display the list: Print the current list of numbers.
# (d) Quit: Exit the program. 

listOfNumbers=[]
while True:
    print("(a) Add a number. \n(b) Remove a number. \n(c) Display the list. \n(d) Quit.")
    choice=input("Please enter a choice(a-d): ")
    
    if choice.lower()=="a":
        #the user should enter an integer
        try:
            number=int(input("Please enter and integer: "))
            listOfNumbers.append(number)
            print("Number added successfully.")
        except ValueError as error:
            print(error)
            print("Error: Please enter a valid integer.")
    elif choice.lower()=="b":
        try:
           index=int(input("please enter an index of the number you want to remove: "))
           listOfNumbers.pop(index)
           print("Number removed successfully.")
        except ValueError:
            print("Error: Please enter a valid integer.")
        except IndexError:
            print("Error: That Index doesn't exist in the list")
    elif choice.lower()=="c":
             print(listOfNumbers)
    elif choice.lower()=="d":
            break
    else: 
        print("Invalid choice. Please enter a number from a to d.")
        
   
        

