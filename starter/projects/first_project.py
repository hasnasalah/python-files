 #the dictionnary that will store all contact names and numbers
def load_contacts():
    dictionary = {}
    try:
        # getting the file if not existed create one
        file = open("contacts.txt", "r")
        for line in file:
            name, phone = line.strip().split(",", 1)
            #load data into a dic if a name is already in dict just add another number otherwise create a new value and key
            if name in dictionary:
                dictionary[name].append(phone)
            else:
                dictionary[name] = [phone]

        file.close()
   
    except FileNotFoundError:
        print("file not found")
        
    return dictionary
contac_book=load_contacts()

#function to save the contacts into file 
def save_contacts(dictionary):
    file = open("contacts.txt", "w")

    for name, phones in dictionary.items():
        for phone in phones:
            file.write(name + "," + phone + "\n")

    file.close()

# function that will add the contact
def add_contact(dictionary):
    name = input("Please enter the name: ")
    #check if contact name existed:
    if name in dictionary:
       answer = input(
            "This contact already exists. "
            "Add another phone number? (y/n): "
        ).lower()
       if answer != "y":
            print("Contact was not changed.")
            return
    #validate the phone number
    while True:
        try:
            phone = input("Please enter a 10-digit phone number: ")
            if len(phone) != 10 or not phone.isdigit():
                raise ValueError("Phone number must be valid (10 digits)!!")
            break
        except ValueError as error:
            print(error)

    if name in dictionary:
        dictionary[name].append(phone)
    else:
        dictionary[name] = [phone]
    save_contacts(dictionary)
    print("Contact added successfully!")

#function to display the contacts
def display_contacts(dictionary):
    print("\n" + "=" * 32)
    print("         CONTACT DETAILS")
    print("=" * 32)
    if not dictionary:
        print("No Contacts Found")
    else:   
        for name, phones in sorted(dictionary.items()):
          print(f"\nName: {name}:")
          for phone in phones:
            print(f"  -{phone}")
          print("-" * 32)

#function to delete a contact
def delete_contact(dictionary):
     search=input("Enter the contact name you want to delete:")
     if search in dictionary:
        del dictionary[search]
        save_contacts(dictionary)
        print("Contact deleted successfully!")
     else:
         print("Contact was not found!")

#function to search for a contact
def seach_contact(dictionary):
    search = input("Enter the contact name you want to search for: ")

    if search in dictionary:
        print("\n" + "=" * 32)
        print("         CONTACT DETAILS")
        print("=" * 32)

        print("Name:", search)

        for phone in dictionary[search]:
            print("  -", phone)

        print("-" * 32)

    else:
        print("Contact was not found!")
        
        
while True:
  print("Contact Book Menu: \n1. Add New Contact\n2. View All Contacts.\n3. Search Contact.\n4. Delete Contact\n5. Exit")
  choice=input("Enter your choice (1-5):")
  if choice=="1":
     add_contact(contac_book)
  elif choice=="2":
   display_contacts(contac_book)
  elif choice=="3":
    seach_contact(contac_book)
  elif choice=="4":
   delete_contact(contac_book)
  elif choice=="5":
    print("you are quiting the program....")
    break
  else:
        print("Invalid choice. Please enter a number from 1 to 5.")
            
            