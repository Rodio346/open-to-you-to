#Write a script that will ask for the sides of a rectangular and print out the area. Provide error messages if either of the sides is negative.

length = int(input("Enter length "))
Breadth = int(input("Enter Breadth"))
if length>0 and Breadth > 0:
    print("The Area is ", length*Breadth)
else:
    print("Length is negative" if length <0 else "Breadth is negative") #ternary operator style is used here instead of conventional if else