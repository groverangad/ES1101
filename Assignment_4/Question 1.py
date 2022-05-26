marks=int(input(' Insert marks awarded to student '))

if marks in range(0,25):
    grade_awarded='F'
    
elif marks in range(25,45):
    grade_awarded='E'
    
elif marks in range(45,50):
    grade_awarded='D'

elif marks in range(50,60):
    grade_awarded='C'
    
elif marks in range(60,80):
    grade_awarded='B'
    
elif marks in range(80,101):
    grade_awarded='A'
   
else:
    print("Error : Maximum marks = 100 ")
    
print("Grade awarded to stdudent is ",grade_awarded)

    
    
    
    