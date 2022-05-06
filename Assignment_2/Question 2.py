'''Question 2
Store your name, SID, department name and CGPA into different variables.
With the help of String formatting print the following output:
Hey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is 9.9'''


name="Angad Singh Grover"
SID="21107028"
department="Mechanical Engineering"
cgpa=9
print("Hey, ",name," here!","\n","My SID is ",SID, "\n","i am from ",department,"and my CGPA is ",cgpa)

input_string=input("Enter string: ")
substring="name"
if substring in input_string:
  print("Yes")
else:
  print("No")
