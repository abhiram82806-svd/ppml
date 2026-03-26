#bar plot
import matplotlib.pyplot as plt
categorie = ['a','b','c','d']
values = [3,7,8,5]
plt.bar(categorie,values,color='g',label="bar data")
plt.title("bar plot")
plt.xlabel("categories")
plt.ylabel("values")
plt.legend()
plt.show()
