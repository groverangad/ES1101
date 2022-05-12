print('''Welcome to The calculator. Please choose the operation
      
     1 - Addition
     2 - Subtraction
     3 - Multiplication
     4 - Division ''')

operation = int(input("operation operations form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if operation == 1:
    print(number_1, "+", number_2, "=",number_1+number_2)
                   
  
elif operation == 2:
    print(number_1, "-", number_2, "=",number_1-number_2)
                   
  
elif operation == 3:
    print(number_1, "*", number_2, "=",number_1*number_2)
                    
  
elif operation == 4:
    print(number_1, "/", number_2, "=", number_1/number_2)
else:
    print("Invalid input")