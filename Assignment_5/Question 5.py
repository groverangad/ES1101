asciichr = 65

# Outer loop for ith rows
for i in range(0,6):
    # Inner loop for jth columns
    for j in range(0,i+1):
        char = chr(asciichr)
        print(char,end="")
        asciichr += 1
    print()