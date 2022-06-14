n=5
#Outer loop
for i in range(n):
    #Inner loop
	    for j in range(i):
	        print ('*', end=" ")
	    print('')
	#Repeated with different step
for i in range(n,0,-1):
	    for j in range(i):
	        print('*', end=" ")
	    print('')