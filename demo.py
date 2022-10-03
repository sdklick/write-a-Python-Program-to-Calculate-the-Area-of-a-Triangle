# write a Python Program to Calculate the Area of a Triangle

side1=int(input("please input first side value : "))
side2=int(input("please input second side value :  "))
side3=int(input("please input third side value : "))

semip=(side1+side2+side3)/2

area= semip*(semip-side1)*(semip-side2)*(semip-side3)

finalarea=area**0.5

print(finalarea)
