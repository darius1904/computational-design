#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: darius
"""
#a width
#b length
#c height

a=int(input("Enter the width of a room in meters: "))
b=int(input("Enter the length of the room in meters: ")) 
c=int(input("Enter the height of the room in meters: "))  

v=a*b*c
ar=a*b
print("\nThe volume of the room is", v,"m^3")
print("The area of the room is", ar,"m^2")
print("The volume of the room is", int(v*1e9),"mm^3")
print("The area of the room is", int(ar*1e6),"mm^2")

if a > b and a > c:
    print("The width of your room surpasses both its length and height.")
elif b > a and b > c:
    print("The length of your room surpasses both its width and height.")
elif c > a and c > b:
    print("The height of your room surpasses both its width and length.")
else:
    print("Two or more dimensions are equal — no single dominant dimension.")