#wap to draw the 3d plot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x = [1,2,3,4,5]
y = [5,6,7,8,9]
z= [2,3,3,3,2]
ax.scatter(x,y,z,color='r',label = "3D points")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_zlabel("x-axis")
plt.legend()
plt.show()