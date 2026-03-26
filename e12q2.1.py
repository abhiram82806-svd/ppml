#wap to draw the scatter and bar plot
#scatter plot
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y=[5,7,6,8,7]
plt.scatter(x,y,color='b',label="scatter points ")
plt.title("SCATTER PLOT")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()