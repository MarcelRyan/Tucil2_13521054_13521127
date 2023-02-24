import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import closestPoint

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
array_of_points = closestPoint.input3D()
idx_min = closestPoint.minDistanceBruteForce(array_of_points)

for i in range(len(array_of_points)):
    if (i == idx_min * 2 or i == idx_min * 2 + 1):
        ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "red")
    else:
        ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "blue")


plt.plot([array_of_points[idx_min*2][0] ,array_of_points[idx_min*2+1][0]] , [array_of_points[idx_min*2][1], array_of_points[idx_min*2+1][1]], [array_of_points[idx_min*2][2], array_of_points[idx_min*2+1][2]], color = 'black',  linestyle = '-')
plt.ioff()
plt.show()