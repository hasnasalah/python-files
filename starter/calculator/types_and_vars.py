name="hasna"
age=32
height=1.59
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")
ageInfive=age+5
print(f"In 5 years, I will be {ageInfive} years old.")
#Calculate the area of a rectangle with width = 5.5 and height = 2 
# (you can hardcode these numbers or store them in variables).
# Print the result in a formatted sentence:
# "The area of a 5.5 x 2 rectangle is 11.0."
width=5.5
heightofRec=2
print(f"The area of a {width}x {heightofRec} rectangle is {width*heightofRec}.")
# in this one i want to demonstate the use of string concatination:
minus="-"
plus="+"
line="|"
space=" "

top_bottom = plus + minus * 6 + plus
middle = line + space * 6 + line

print("\n",top_bottom,"\n",middle,"\n",middle,"\n",middle,"\n",middle,"\n",middle,"\n",top_bottom)
