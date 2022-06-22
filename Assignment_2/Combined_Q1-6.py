#Q1

Given_string="python is a case sensitive language"
String_length=len(Given_string)
Reverse_string=Given_string[-1::-1]
New_string=Given_string[10::27]
replacestring=Given_string.replace("a case sensitive","object oriented")
Position_a=Given_string.index("a")
String_nospace=Given_string.replace(" ","")
print(String_length,Reverse_string,New_string,replacestring,Position_a,String_nospace)

#Q2
name="Angad Singh Grover"
SID="21107028"
department="Mechanical Engineering"
cgpa=9
print("Hey, ",name," here!","\n","My SID is ",SID, "\n","i am from ",department,"and my CGPA is ",cgpa)

#Q3
input_string=input("Enter string: ")
substring="name"
if substring in input_string:
  print("Yes")
else:
  print("No")
  
  
#Q4
a=56
b=10
print("a&b=", a & b)

print("a|b=", a | b)
print("a^b", a ^ b)

print("a << 2 : ", a << 2, " and b << 2: ", b << 2)

print("a >> 2 :", a >> 2, " and b >> 4:", b >> 4)


#Q5
A1=first_number=int(input("enter side 1: "))
A2=second_number=int(input("enter 2nd side: "))
A3=third_number=int(input("enter 3rd side: "))
while (A1+A2<=A3) or (A2+A3<=A1) or (A3+A1<=A2):
  print("No")
  break
while (A1+A2>A3) and (A2+A3>A1) and (A3+A1>A2):
  print("Yes")
  break


#Q6
a=int(input("enter first number here"))
b=int(input("enter second number here"))

diff=bin(a^b)

flipped_bits= diff.count(1)
print(flipped_bits)





