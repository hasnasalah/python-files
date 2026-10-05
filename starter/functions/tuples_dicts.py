months=("January","February","March","April","May","June","July",
        "August","September","October","November","December")
print("First month: ",months[0])
print("Last month: ",months[-1])

#demonstarte that tuples are immutable

try:
    months[0]="first month"
except TypeError as error_message:
    print(f"Tuples are immutable, error: {error_message}")
    
 # Create a dictionnary   
students={"Anna":95,"Canan":59,"Omar":100,"Ahmed":100,"Anne":60}
students["Rana"]=55
print(students)

# update a value 
students.update({"Omar":33})
# display the dictionnary items 
for student, grade in students.items():
    print(student,": ",grade)
