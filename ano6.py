def power(a,n):
    if n==0:
        return 1 
    else:
        return a*power(a,n-1)
x = int(input ("enter your number : "))
y = int(input ("enter your number : "))
print(power(x,y))