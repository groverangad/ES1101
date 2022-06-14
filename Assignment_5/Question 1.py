inputstring=input("Enter string here :")
#Creating empty string
revstring=""

#Each element from inputstring is added from left side 
for i in inputstring:
    revstring=i+revstring

print(revstring)        