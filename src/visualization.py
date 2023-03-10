import matplotlib.pyplot as plt
import closestPoint
import time
import os

os.system('cls')
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
print("Selamat datang di program mencari pasangan titik terdekat pada dimensi ke-n !")
print("Input Process")
print(
    """
There is 2 ways to input
1. Random
2. Manual 
Please include the number and it is not validated so recheck before you press enter!
    """
)
inputChoice = int(input("How do you wanna input : "))
while (inputChoice > 2 or inputChoice < 1):
    print("Input tidak valid silakan input pilihan antara 1 dan 2 saja")
    inputChoice = int(input("How do you wanna input : "))
array_of_points, dimensi = closestPoint.inputUser(inputChoice)
point1, point2 = closestPoint.minDistanceBruteForce(array_of_points, dimensi)
start = time.time()
mindnc, arraydnc  = closestPoint.divideAndConquer(array_of_points, dimensi)
end = time.time()
idx1, idx2 = closestPoint.indexPoint(arraydnc, array_of_points)
print('')
print("Dengan menggunakan algoritma divide and conquer didapat hasil sebagai berikut :")
print("Titik 1: (", end='')
for i in range(dimensi):
    if (i == dimensi - 1):
        print(f"{array_of_points[idx1][i]:.3f})")
    else:
        print(f"{array_of_points[idx1][i]:.3f}, ", end= '')
print("Titik 2 : (", end='')
for i in range(dimensi):
    if (i == dimensi - 1):
        print(f"{array_of_points[idx2][i]:.3f})")
    else:
        print(f"{array_of_points[idx2][i]:.3f}, ", end= '')
print(f"Waktu : {(end-start) * 1000:.3f} ms")
closestPoint.jumlahEucDNC()
print(f"Jarak antar titik : {mindnc:.3f}")
print("Apabila terdapat perbedaan titik, namun jarak euclidean sama hal ini mungkin terjadi apabila ada 2 pasangan titik yang memiliki jarak euclidean yang sama")

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