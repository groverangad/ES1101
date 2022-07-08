#Question 1

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(Number," is a perfect number")
else:
    print(Number," is not a perfect number")


#Question 2

def palindrome(string):
    rev_string=string[::-1]
    print(rev_string)
    if string==rev_string:
        print("entered string is a palindrome")
    else:
        print("entered string is not a palindrome")

user_string=str(input("enter a word, phrase or sentence: "))
palindrome(user_string)





#Question 3

from math import factorial

n=5
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range (i+1):
        print(factorial(i) // (factorial(i-k)*factorial(k)) , end=" ") # nCr = n! / ((n-r)! * r!)
    print()



#Question 4



def checkpanagram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char in str.lower():
            return True
        else:
            return False
        
input_string=input("Enter chosen string here ")
if checkpanagram(input_string.lower())==True:
    print(input_string," is a panagram")
else:
    print(input_string, " is not a panagram ")
    
    
    
#Question 5


input_string=input("Enter string with hyphen seperated sequence ")
items=[input_string.split('-')]
items.sort()
print('-'.join(items))


#Question 6


def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Aayush","Civil",21102050)


#Question 7


class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()


#Question 8


def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	
	if (found == False):
		print(" not exist ")


arr = [0, -1, 2, -3, 1]
n = len(arr)
findTriplets(arr, n)



#Question 9


class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")























