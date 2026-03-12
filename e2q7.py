num_int = int(input("enter the int values : "))
num_flo = float(input("enter the float value : "))
num_bool = input("enter the bbolean value : ")
text = input("enter the strig : ")
num_com = complex(input("enter the complex value :"))

if num_bool == "True" : 
    num_bool = True 
else :
    num_bool= False

print("the types of the values are ")
print(type(num_int))
print(type(num_flo))
print(type(num_bool))
print(type(text))
print(type(num_com))