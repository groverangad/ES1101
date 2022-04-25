Question_5= "Write a program that prints out the sine and cosine of the angles"\
    "ranging from 0 to 345◦ in 15◦ increments."\
        "Each result should be rounded to 4 decimal places."
        
print(Question_5,"")
    
import math


for i in range(0,360,15):
    

        sine_value=math.sin(math.radians(i))
        
        cosine_value=math.cos(math.radians(i))
        
        print("sin",i,"=",round(sine_value,4),"    cos",i,"=",round(cosine_value,4))
        
        
        
        
        
        