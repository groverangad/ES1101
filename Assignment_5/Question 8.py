

Testlist=[]

for i in range(10):
    Testlist.append(int(input("Enter number: ")))
    
print(Testlist)

a=('''
      Press 1 for positive numbers
      Press 2 for negative numbers
      Press 3 for odd numbers 
      Press 4 for even numbers
      Press 5 for checking frequency of numbers ''')
print(a)
      
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
    for j in Testlist:
        if j%2!=0:
            print(j)
elif operation==4:
    for j in Testlist:
        if j%2==0:
            print(j)
elif operation==5:
    Testdic={num:Testlist.count(num) for num in Testlist}
    print(Testdic)
    



        
    