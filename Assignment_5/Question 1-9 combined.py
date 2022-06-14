'''Question 1'''

inputstring=input("Enter string here :")
#Creating empty string
revstring=""

#Each element from inputstring is added from left side 
for i in inputstring:
    revstring=i+revstring

print(revstring)        

'''Question 2'''
lowlimit=int(input("Insert lower limit for range: "))
upperlimit=int(input("Insert upper limit for range: "))

givennum=int(input("Insert chosen number for checking multiples: "))

for i in range (lowlimit,upperlimit):
    if i%givennum==0:
        print(i)
    else:
        continue
    
print("No more multiples")   

     
    
'''Question 3'''

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
  
    
  
'''Question 4''' 
    
n=5
#Outer loop
for i in range(n):
    #Inner loop
	    for j in range(i):
	        print ('*', end=" ")
	    print('')
	#Repeated with different step
for i in range(n,0,-1):
	    for j in range(i):
	        print('*', end=" ")
	    print('')
   
        
   
    
'''Question 5'''      
    
asciichr = 65

# Outer loop for ith rows
for i in range(0,6):
    # Inner loop for jth columns
    for j in range(0,i+1):
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
    print()
    
    
    
'''Question 6'''   

#Taking upper and lower limit values
lowlimit=int(input("Insert lowlimit limit for range: "))
upperlimit=int(input("Insert upperlimit limit for range: "))

print("Prime numbers between", lowlimit, "and", upperlimit, "are:")

for num in range(lowlimit, upperlimit + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)



'''Question 7'''

#Checking multiples if 7 and divisibility by 11
for i in range(0,500):
    if i%7==0 and i%11==0:
        print(i)
    else:
        continue
    
    
    
'''Question 8'''    

#Creating blank list
Testlist=[]
#Taking 10 values from user
for i in range(10):
    Testlist.append(int(input("Enter number: ")))
    
print(Testlist)

print('''
      Press 1 for positive numbers
      Press 2 for negative numbers
      Press 3 for odd numbers 
      Press 4 for even numbers
      Press 5 for checking frequency of numbers ''',"\n")
      
operation=int(input("Please choose output "))

if operation==1:
    for j in Testlist:
        if j>0:
            print(j)
elif operation==2:
    for j in Testlist:
        if j<0:
            print(j)
elif operation==3:
    #Checking for odd numbers
    for j in Testlist:
        if j%2!=0:
            print(j)
elif operation==4:
    #Checking for even numbers
    for j in Testlist:
        if j%2==0:
            print(j)
elif operation==5:
    #Converting list to dictionary and using count
    Testdic={num:Testlist.count(num) for num in Testlist}
    print(Testdic)
    


'''Question 9'''
#Creating empty list
Testlist=[]
#Taking 10 inputs from user and then adding them to list
for i in range(10):
    Testlist.append(input("Enter word: "))
print(Testlist)
#Converting list to dictionary and then using count 
Testdic={word:Testlist.count(word) for word in Testlist}

print(Testdic)