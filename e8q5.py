n = int(input("enter the number "))
def prime_check(n):
    count=0
    for i in range (1,n):
        if(n%i == 0):
            count=count+1
        return count
count = prime_check(n)
if count ==2:
    print("prime no ")
else: 
    print("not a prime no")
        