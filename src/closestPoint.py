import random
import math

def inputUser():
    n = int(input("Masukkan berapa titik yang ingin di generate: "))
    dimensi = int(input("Ingin berapa dimensi: "))
    array = []
    for i in range(n):
        points = []
        for j in range(dimensi):
            points.append(random.uniform(0, 10))
        array.append(points)
    return array, dimensi

def minDistanceBruteForce(array, dimensi):
    array_distance = []
    for i in range(len(array)):
        temp = []
        for j in range(i+1, len(array)):
            jarak = 0
            for k in range(dimensi):
                jarak += (array[j][k] - array[i][k]) ** 2
            temp.append(math.sqrt(jarak))
        array_distance.append(temp)
    min = array_distance[0][0]
    point1= 0
    point2 = 0
    print(array_distance)
    for i in range(len(array_distance)):
        for j in range(len(array_distance[i])):
            if (min > array_distance[i][j]):
                min = array_distance[i][j]
                point1 = i
                point2 = j+i+1
    return point1, point2



