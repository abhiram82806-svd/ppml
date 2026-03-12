m = int(input("enter you maths marks : "))
s = int(input("enter you ss marks : "))
x = int(input("enter you sns marks : "))
z = int(input("enter you gk marks : "))
c = int(input("enter you de marks : "))

per = ((m+s+x+z+c)/500)*100

if(per >=90 and per <=100):
    print("grade is O")
elif(per >=80 and per <=90):
    print("grade is e")
elif(per >=70 and per <=80):
    print("grade is a")
elif(per >=60 and per <=70):
    print("grade is b")
elif(per >=50 and per <=60):
    print("grade is c")
else:
    print("fail")