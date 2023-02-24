import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import closestPoint

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
array_of_points, dimensi = closestPoint.inputUser()
point1, point2 = closestPoint.minDistanceBruteForce(array_of_points, dimensi)

if (dimensi == 3):
    for i in range(len(array_of_points)):
        if (i == point1 or i == point2):
            ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "red")
        else:
            ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "blue")


    plt.plot([array_of_points[point1][0] ,array_of_points[point2][0]] , [array_of_points[point1][1], array_of_points[point2][1]], [array_of_points[point1][2], array_of_points[point2][2]], color = 'black',  linestyle = '-')
    plt.ioff()
    plt.show()