'''Question 4
Write a python program to check if the word “name” is present in the string
entered by the user (Print : “Yes” or “No”).'''


input_string=input("Enter string: ") 

substring="name"

if substring in input_string:
    
  print("Yes")
else:
  print("No")
