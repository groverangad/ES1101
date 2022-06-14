
A1=first_number=int(input("enter side 1: "))
A2=second_number=int(input("enter 2nd side: "))
A3=third_number=int(input("enter 3rd side: "))

semipem=(A1+A2+A3)/2

Area = ((semipem)*(semipem-A1)*(semipem-A2)*(semipem-A3))**(0.5)

if (A1+A2<=A3) or (A2+A3<=A1) or (A3+A1<=A2):
  print("No")
  check=0

if (A1+A2>A3) and (A2+A3>A1) and (A3+A1>A2):
   check=1
   print("Yes")

if check==1:
    print("Area of triangle is ",Area)
else:
    print("invalid triangle ")
    
    
    