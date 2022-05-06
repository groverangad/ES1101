'''Question 6
Given two numbers ‘a’ and b’. Write a program to count number of bits
needed to be flipped to convert ‘a’ to ‘b’.'''

a=int(input("Enter first number here "))
b=int(input("Enter second number here "))

diff=str(bin(a^b))

flipped_bits= diff.count("1")

print(flipped_bits)
