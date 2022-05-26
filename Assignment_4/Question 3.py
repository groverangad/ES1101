import random

a=random.randint(0,100)
b=random.randint(0,100)
print(a,"*",b,"= ?")
c=a*b
answer=int(input(" Enter your answer here "))

if answer==c:
    print("Answer is correct ")
    
else:
    print(" Answer is incorrect","\n","The correct answer is ",c)

