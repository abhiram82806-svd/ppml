def largest(a,b,c):
    if(a>b and a>c):
        return a
    elif b>=a and b>=c : 
        return b
    else:
        return c
x= int(input("enter a number :")) 
y = int(input("enter a number :"))                          
z = int(input("enter a number :"))
print(largest(x,y,z))      