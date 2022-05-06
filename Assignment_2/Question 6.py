#Question 6

a=int(input("Enter first number here "))
b=int(input("Enter second number here "))

diff=str(bin(a^b))

flipped_bits= diff.count("1")

print(flipped_bits)
