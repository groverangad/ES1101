#Question 5


A1=first_number=int(input("enter side 1: "))
A2=second_number=int(input("enter 2nd side: "))
A3=third_number=int(input("enter 3rd side: "))

while (A1+A2<=A3) or (A2+A3<=A1) or (A3+A1<=A2):
  print("No")
  break

while (A1+A2>A3) and (A2+A3>A1) and (A3+A1>A2):
  print("Yes")
  break
