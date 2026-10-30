import calendar
from datetime import date
# Display today's date

print("*"*20)
print("Today's Date: ")
today=date.today()
print(today)

while(True):
  try: 
      
      month=int(input("please enter a a month: \n"))
      year=int(input("Please enter a year: \n"))
      if month>12 or month<0:
            print("this is not valid month")
            continue
      elif year<=0:
          print("this is not valid")
          continue
      break
  except ValueError:
      print("Please Enter a Valid date!!\n")
      
print("*"*20)
print(f"this the calendar for {calendar.month_name[month]} and {year}: ")
print(calendar.month(year, month))


#Check whether today falls within the selected month and year
if today.year == year and today.month == month:
    print(f"Today is {today.strftime('%B %d, %Y')}!")
else:
    print(f"Today does not fall in {calendar.month_name[month]} {year}.")

print("*"* 40)

   
