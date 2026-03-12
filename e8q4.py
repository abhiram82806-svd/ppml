def fact (n,fact):
    
    for i in range (1,n+1):
        fact = fact*1
    
n = int(input("enter the number : "))
result = fact(n,1)
print("the factorial is ",fact)