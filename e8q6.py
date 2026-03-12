def reversed_str(str):
    reversed_str=" "
    for i in str:
        reversed_str=i+reversed_str
    print(reversed_str)
str=input("enter a string :")
reversed_str(str)