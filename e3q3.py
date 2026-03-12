x = int(input("enter the 1st value : "))
y = int(input("enter the 2nd value : "))
z = int(input("enter the 3rd value : "))

if(x>y and x>z):
    print("x is greatest")
elif(y>x and y>z):
    print(f"y is greatest")
else : 
    print("z is greatest")
