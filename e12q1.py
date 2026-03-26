#WAP TO PLOAT A SAMPLE GRAPH USING PLOT()
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.title("sample lineplot")
plt.plot(x,y,linestyle='--',color='r',marker='o',label="data line")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()