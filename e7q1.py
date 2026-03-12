m = int(input("enter your num : "))
n = int(input("enter your num : "))

list1 = []
for i in range(m, n + 1):
    list1.append(i)

print(list1)

# smallest element
smallest = list1[0]
for i in range(len(list1)):
    if list1[i] < smallest:
        smallest = list1[i]

# sum and average
total = sum(list1)
avg = total / len(list1)

print("smallest element :", smallest)
print("avg :", avg)
print("sum :", total)
