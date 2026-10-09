 #the dictionnary that will store all contact names and numbers
contac_book={}
while True:
  print("Contact Book Menu: \n1. Add New Contact\n2. View All Contacts.\n3. Search Contact.\n4. Delete Contact\n5. Exit")
  choice=int(input("Enter your choice (1-5):"))

# function that will add the contact
  def add_contact(dictionary):
    name = input("Please enter the name: ")
    phone = input("Please enter the phone number: ")
    if name in dictionary:
        dictionary[name].append(phone)
    else:
        dictionary[name] = [phone]

#function to display the contacts
  def display_contacts(dictionary):
     print(" All Contacts: ")
     if not dictionary:
         print("No Contacts Found")
     else:   
        for name, phones in sorted(dictionary.items()):
          print(name + ":")
        for phone in phones:
            print("  -", phone)

#function to delete a contact
  def delete_contact(dictionary):
     search=input("Enter the contact name you want to delete:")
     if search in dictionary:
        del dictionary[search]
  if choice==1:
     add_contact(contac_book)
  elif choice==2:
   display_contacts(contac_book)
  elif choice==3:
    search=input("Enter the name your searching for....")
    for name,contact in contac_book.items():
        if search==name:
            print(name,": ",contact)
  elif choice==4:
   delete_contact(contac_book)
  elif choice==5:
    print("you are quiting the program....")
    break
  else:
        print("Invalid choice. Please enter a number from 1 to 5.")
            
            