#This book is for sale at http://leanpub.com/python-examples
#This version was published on 2020-05-28

# I am going to follow this book till end whenever I have time. Although I should be able to complete it in few months lets see 

#Exercise : Calculation 
#1
width = 24 
height = 30
area = width * height
circumference = 2 * ( width + height)

print( " Area of the Rectangle is = " , area)
print(" Perimeter of the Rectangle is =" , circumference)

#2 
radius = int(input("Enter the Radius "))
print("Area of the circle =", 3.14 * radius * radius)
print("Circuference of the circle =", 2 * 3.14 * radius)

#2 WITH  math import 
import math 

print("Area of the circle =", math.pi * radius * radius)
print("Circuference of the circle =", 2 * math.pi * radius)

#3 
a = int(input(" Enter a number "))
b = int(input("Enter another Number "))
print( a+b," ", a-b," ", a/b ," ", a*b )