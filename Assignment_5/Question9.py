#Creating empty list
Testlist=[]
#Taking 10 inputs from user and then adding them to list
for i in range(10):
    Testlist.append(input("Enter word: "))
print(Testlist)
#Converting list to dictionary and then using count 
Testdic={word:Testlist.count(word) for word in Testlist}

print(Testdic)