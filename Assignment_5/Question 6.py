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
