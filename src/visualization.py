import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import closestPoint
import time

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
array_of_points, dimensi = closestPoint.inputUser()
point1, point2 = closestPoint.minDistanceBruteForce(array_of_points, dimensi)
start = time.time()
mindnc, arraydnc  = closestPoint.divideAndConquer(array_of_points, dimensi)
end = time.time()
idx1, idx2 = closestPoint.indexPoint(arraydnc, array_of_points)
print(f"Titik terdekat dengan algoritma divide and conquer {idx1+1} dan titik {idx2+1} dengan jarak sebesar {mindnc}")
print(f"waktu yang dibutuhkan algoritma divide and conquer adalah {end-start}")
closestPoint.jumlahEucDNC()
print("Apabila terdapat perbedaan titik, namun jarak euclidean sama hal ini mungkin terjadi apabila ada 2 pasangan titik yang memiliki jarak euclidean yang sama")
# print(f"Jumlah operasi euclidean distance algoritma divide and conquer adalah {count}")

if (dimensi == 3):
    for i in range(len(array_of_points)):
        if (i == idx1 or i == idx2):
            ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "red")
        else:
            ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], c= 'b')


    plt.plot([array_of_points[idx1][0] ,array_of_points[idx2][0]] , [array_of_points[idx1][1], array_of_points[idx2][1]], [array_of_points[idx1][2], array_of_points[idx2][2]], color = 'black',  linestyle = '-')
    plt.ioff()
    plt.title("3D Scatter Plot")
    ax.set_xlabel("Sumbu X")
    ax.set_ylabel("Sumbu Y")
    ax.set_zlabel("Sumbu Z")
    plt.show()