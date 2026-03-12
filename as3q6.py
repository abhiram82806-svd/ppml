#wap to remove all duplicateas from a given string
x = input("enter the string:")
result=""
for char in x:
    if char not in result:
        result=result+char
print(result)

