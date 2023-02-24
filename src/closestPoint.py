import random
import math
import numpy as np
import sys

def inputUser():
    n = int(input("Masukkan berapa titik yang ingin di generate: "))
    dimensi = int(input("Ingin berapa dimensi: "))
    array = []
    for i in range(n):
        points = []
        for j in range(dimensi):
            points.append(random.uniform(0, 10))
        array.append(points)
    for i in range(n):
        min_idx = i
        for j in range(min_idx+1, n):
            if (array[min_idx][0] > array[j][0]):
                min_idx = j
        temp = array[min_idx]
        array[min_idx] = array[i]
        array[i] = temp
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
    for i in range(len(array_distance)):
        for j in range(len(array_distance[i])):
            if (min > array_distance[i][j]):
                min = array_distance[i][j]
                point1 = i
                point2 = j+i+1
    print(f"Titik terdekat dengan algoritma bruteforce adalah titik {point1} dan titik {point2} dengan jarak sebesar {min}")
    return point1, point2

def distance(point1, point2, dimensi):
    jarak = 0
    for i in range(dimensi):
        jarak += (point2[i] - point1[i]) ** 2
    return math.sqrt(jarak)

def divideAndConquer(points, dimensi):
    array = []
    if (len(points) == 2):
        array = points
        min = distance(points[0], points[1], dimensi)
        return min, array
    else:
        mid = len(points)//2
        left = []
        right = []
        # Membagi titik menjadi dua himpunan kanan kiri. Dengan syarat titik sudah terurut menaik berdasarkan sumbu x
        for i in range(mid):
            left.append(points[i])
        for i in range(mid, len(points)):
            right.append(points[i])
        minLeft, arrayLeft = divideAndConquer(left, dimensi)
        minRight, arrayRight = divideAndConquer(right, dimensi)
        if (minLeft < minRight):
            min = minLeft
            array = arrayLeft
        else:
            min = minRight
            array = arrayRight
        
        # Kondisi dimana ada titik pada himpunan kiri dan kanan yang jaraknya kemungkinan lebih kecil dari minLeft atau minRight

        midPoint = []
        # Mengambil titik yang jarak x nya lebih kecil atau sama dengan min dari titik x median
        for i in range(len(points)):
            if (abs(points[i][0] - points[mid][0]) <= min):
                midPoint.append(points[i])
        
        # Mengurutkan titik berdasarkan y menurun
        for i in range(len(midPoint)):
            min_idx = i
            for j in range(min_idx+1, len(midPoint)):
                if (points[min_idx][1] < points[j][1]):
                    min_idx = j
            temp = points[min_idx]
            points[min_idx] = points[i]
            points[i] = temp
        
        for i in range(len(midPoint)):
            for j in range(i+1, len(midPoint)):
                proses = True
                for k in range(dimensi):
                    if (abs(midPoint[i][k] - midPoint[j][k]) > min):
                        proses = False
                        break
                if (proses):
                    minMid = distance(midPoint[i], midPoint[j], dimensi)
                    if (minMid < min):
                        min = minMid
                        array = [midPoint[i], midPoint[j]]
        return min, array

def indexDNC(array, points):

    for i in range(len(points)):
        if (points[i] == array[0]):
            idx1 = i
        if (points[i] == array[1]):
            idx2 = i
    return idx1, idx2
