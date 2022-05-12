import math
from math import pi
from math import cos
from math import sin

print((3 + 4) * 5)
n = int(input('Enter a number: '))
print(n*(n-1)/2)
r = float(input('Enter another number: '))
print(4 * pi * r**2)
a = float(input('Enter 2 more numbers:'))
b = float(input())
print((r * cos(a)**2 + r * sin(b)**2) ** 0.5 )

y2 = float(input('Enter 4 more numbers: '))
y1 = float(input())
x2 = float(input())
x1 = float(input())

print((y2 - y1) / (x2 - x1))