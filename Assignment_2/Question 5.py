'''Question 5
For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”).[Don’t use if else here].'''

A1=first_number=int(input("enter side 1: "))
A2=second_number=int(input("enter 2nd side: "))
A3=third_number=int(input("enter 3rd side: "))

while (A1+A2<=A3) or (A2+A3<=A1) or (A3+A1<=A2):
  print("No")
  break

while (A1+A2>A3) and (A2+A3>A1) and (A3+A1>A2):
  print("Yes")
  break
