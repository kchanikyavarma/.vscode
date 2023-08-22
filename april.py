a= int(input("enter the number"))
b= int(input("enter the number"))
c= int(input("enter the number"))

if a > b and a > c:
    print("Largest number is",a)
elif b > a and b > c:
    print("Largest number is",b) 
else:
    print("Largest number is",c)  