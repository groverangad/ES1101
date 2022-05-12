
Number=int(input("Enter a number: "))
Num_bin=[]
while(Number>0):
    Bin_digit=Number%2
    Num_bin.append(Bin_digit)
    Number=Number//2
Num_bin.reverse()
print("Binary Equivalent is: ")
for i in Num_bin:
    print(i,end=" ")
