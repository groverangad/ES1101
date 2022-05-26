import random

number_1=random.randint(0,100)
number_2=random.randint(0,100)
print(number_1,"*",number_2,"= ?")
num_result=number_1*number_2
answer=int(input(" Enter your answer here "))

if answer==num_result:
    print("Answer is correct ")
    
else:
    print(" Answer is incorrect","\n","The correct answer is ",num_result)

