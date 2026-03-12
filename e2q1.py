p = float(input("enter the value of p :"))
t = float(input("enter the value of t : "))
r  = float(input("enter the value of r: "))

si = (p*t*r)/100

print("the simple intrest is :" , si)

ci = p*(1+r/100)**t

print("the compount intrest is   :" , ci)
