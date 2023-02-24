import random
import math
import numpy as np
import sys
sys.setrecursionlimit(10000)
import time

def inputUser():
    n = int(input("Masukkan berapa titik yang ingin di generate: "))
    dimensi = int(input("Ingin berapa dimensi: "))
    array = []
    for i in range(n):
        points = []
        for j in range(dimensi):
            points.append(random.uniform(0, 100))
        array.append(points)
    # Mengurutkan array dari x axis menaik
    quickSort(array, 0, len(array)-1)
    return array, dimensi

def partition(array, low, high):
    # Quicksort dengan pivot elemen paling kanan
    i = low
    j = high-1
    idxpivot = high//2
    pivot = array[idxpivot][0]
    while (i <= j):
        while (array[i][0] < pivot):
            i += 1
            if (i >= high):
                break 
        while (array[j][0] >= pivot):
            j -= 1
            if (j <= low):
                break
        if (i < j):
            (array[i], array[j]) = (array[j], array[i])
    (array[i], array[high]) = (array[high], array[i])
 
    # Mengembalikan indeks dilakukannya partisi
    return i
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def minDistanceBruteForce(array, dimensi):
    count = 0
    start = time.time()
    array_distance = []
    arraypoint = []
    for i in range(len(array)):
        temp = []
        for j in range(i+1, len(array)):
            jarak = 0
            for k in range(dimensi):
                jarak += (array[j][k] - array[i][k]) ** 2
            temp.append(math.sqrt(jarak))
            count += 1
        array_distance.append(temp)
    min = array_distance[0][0]
    point1= 0
    point2 = 0
    for i in range(len(array_distance)):
        for j in range(len(array_distance[i])):
            if (min > array_distance[i][j]):
                min = array_distance[i][j]
                point1 = i
                point2 = i+j+1
    end = time.time()
    print(f"Titik terdekat dengan algoritma bruteforce adalah titik {point1+2} dan titik {point2+1} dengan jarak sebesar {min}")
    print(f"Waktu yang diperlukan untuk algoritma bruteforce adalah {end-start}")
    print(f"Jumlah operasi euclidean distance algoritma brute force adalah {count}")
    return point1+1, point2+1
count = 0
def distance(point1, point2, dimensi):
    global count
    jarak = 0
    for i in range(dimensi):
        jarak += (point2[i] - point1[i]) ** 2
    count += 1
    return math.sqrt(jarak)

def divideAndConquer(points, dimensi):
    # Mengurutkan array dari x axis menaik
    quickSort(points, 0, len(points)-1)
    array = []
    if (len(points) == 2):
        array = points
        min = distance(points[0], points[1], dimensi)
        return min, array
    elif (len(points) == 3):
        min1 = distance(points[0], points[1], dimensi)
        min2 = distance(points[0], points[2], dimensi)
        min3 = distance(points[1], points[2], dimensi)
        if (min1 <= min2 and min1 <= min3):
            array = [points[0], points[1]]
            return min1, array
        elif (min2 <= min1 and min2 <= min3):
            array = [points[0], points[2]]
            return min2, array
        else:
            array = [points[1], points[2]]
            return min3, array
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

        # Mencari pasangan titik yang nilai distancenya lebih kecil dari minLeft atau minRight jika ada
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

def jumlahEucDNC():
    print("Jumlah operasi euclidean untuk algoritma divide and conquer adalah", count+1)

def indexPoint(array, points):

    for i in range(len(points)):
        if (points[i] == array[0]):
            idx1 = i
            break
    for i in range(len(points)):
        if (points[i] == array[1]):
            idx2 = i
            break
    return idx1, idx2
