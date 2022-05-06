'''Question1 
For a given input string “Python is a case sensitive language”. Write python
code for the following:
a. Find the length of the input string.
b. Reverse the order of the string in one line code.
c. Using Slice function store “a case sensitive” in new string.
d. Replace “a case sensitive” with “object oriented”.
e. Find index of substring “a” in the given input string.
f. Remove the white spaces from the given input string.'''


Given_string="python is a case sensitive language"

String_length=len(Given_string)

Reverse_string=Given_string[-1::-1]

New_string=Given_string[10::27]

Replacestring=Given_string.replace("a case sensitive","object oriented")

Position_a=Given_string.index("a")

String_nospace=Given_string.replace(" ","")

print(String_length,Reverse_string,New_string,Replacestring,Position_a,String_nospace)
