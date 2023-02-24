import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import closestPoint

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
array_of_points, dimensi = closestPoint.inputUser()
point1, point2 = closestPoint.minDistanceBruteForce(array_of_points, dimensi)
mindnc, arraydnc = closestPoint.divideAndConquer(array_of_points, dimensi)
idx1, idx2 = closestPoint.indexDNC(arraydnc, array_of_points)
print(f"Titik terdekat dengan algoritma divide and conquer {idx1} dan titik {idx2} dengan jarak sebesar {mindnc}")

if (dimensi == 3):
    for i in range(len(array_of_points)):
        if (i == idx1 or i == idx2):
            ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "red")
        else:
            ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "blue")


    plt.plot([array_of_points[idx1][0] ,array_of_points[idx2][0]] , [array_of_points[idx1][1], array_of_points[idx2][1]], [array_of_points[idx1][2], array_of_points[idx2][2]], color = 'black',  linestyle = '-')
    plt.ioff()
    plt.show()