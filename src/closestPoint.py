import random
import math

def inputUser():
    n = int(input("Masukkan berapa titik yang ingin di generate: "))
    dimensi = int(input("Ingin berapa dimensi: "))
    array = []
    for i in range(n):
        points = []
        for j in range(dimensi):
            points.append(random.randint(0, 10))
        array.append(points)
    return array, dimensi

def minDistanceBruteForce(array, dimensi):
    array_distance = []
    for i in range(0, len(array), 2):
        jarak = 0
        for j in range(dimensi):
            jarak += (array[i+1][j] - array[i][j]) **2
        print(math.sqrt(jarak))
        array_distance.append(math.sqrt(jarak))
    
    min = array_distance[0]
    idx_min = 0
    for i in range(len(array_distance)):
        if (min > array_distance[i]):
            min = array_distance[i]
            idx_min = i
            print(idx_min)
    return idx_min



