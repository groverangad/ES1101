lowlimit=int(input("Insert lower limit for range: "))
upperlimit=int(input("Insert upper limit for range: "))

givennum=int(input("Insert chosen number for checking multiples: "))

for i in range (lowlimit,upperlimit):
    if i%givennum==0:
        print(i)
    else:
        continue
    
print("No more multiples")        
    