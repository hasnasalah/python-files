#  that takes a tuple of numeric grades and returns the average. Include a try/except to handle the case 
#  if the tuple is empty (to avoid division by zero), returning None or printing a warning in that case.


def get_average_grade(grades_tuple):
    sum=0
    for grade in grades_tuple:
         sum+=grade
         
    try:
        return sum/len(grades_tuple)
    except ZeroDivisionError:
        return None
    
        
        
math_grades=(78,59,90,95,77,80)
science_grades=(58,96,12,55,98,88)
history_grades=(85,78,69,99,77,98)
language_arts_grades=()


course_grades={"math":math_grades,"science":science_grades,"history":history_grades,
 "English language arts":language_arts_grades}

for course,grade in course_grades.items():
   average=get_average_grade(grade)
   if average is None:
       print(f"No grades entred for {course}")
   else:
       print(f"The average greade for: {course} is: {round(average,0)}")
    
    