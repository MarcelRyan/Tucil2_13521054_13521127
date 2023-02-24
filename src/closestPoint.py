import random
import math

def inputDimensi():
    n = int(input("Masukkan berapa titik yang ingin di generate: "))
    dimensi = int(input("Ingin berapa dimensi: "))
    array = []
    for i in range(n):
        x_axes = random.randint(0, 10)
        y_axes = random.randint(0, 10)
        z_axes = random.randint(0, 10)
        array.append([x_axes, y_axes, z_axes])
    return array

def minDistanceBruteForce(array):
    array_distance = []
    for i in range(0, len(array), 2):
        jarak = 0
        jarak += (array[i+1][0] - array[i][0]) ** 2 + (array[i+1][1] - array[i][1]) ** 2 + (array[i+1][2] - array[i][2]) ** 2
        print(math.sqrt(jarak))
        array_distance.append(math.sqrt(jarak))
    
    min = array_distance[0]
    idx_min = 0
    for i in range(len(array_distance)):
        if (min > array_distance[i]):
            idx_min = i
            print(idx_min)
    return idx_min



