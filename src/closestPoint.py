import random
import math
import sys
import time
sys.setrecursionlimit(10000)

def inputUser(choice):
    print("Selamat datang di program mencari pasangan titik terdekat pada dimensi ke-n !")
    n = int(input("Masukkan berapa titik yang ingin di generate: "))
    dimensi = int(input("Ingin berapa dimensi: "))
    array = []
    if(choice == 1):
            # Making random always different every time it runs
        random.seed(time.time())
        for i in range(n):
            points = []
            for j in range(dimensi):
                randomvalue = random.uniform(0, 100)
                points.append(randomvalue)
            array.append(points)
    elif(choice == 2):
        print("Every component x,y,z seperated by comma")
        for i in range(n):
            print("point{} : ".format(i+1), end="")
            inputStr = input("Input point {}: ".format(i+1))
            inputStrList = inputStr.split(",")
            points = [int(x) for x in inputStrList]
            array.append(points)
    
    # Mengurutkan array dari x axis menaik
    return array, dimensi

def partition(array, low, high):
    pivot = array[high][0]
    i = low - 1
    for j in range(low, high):
        if array[j][0] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
 
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def minDistanceBruteForce(array, dimensi):
    count = 0
    start = time.time()
    array_distance = []
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
    print(f"Titik terdekat dengan algoritma bruteforce adalah titik dengan koordinat x :{array[point1][0]:.3f}, y :{array[point1][1]:.3f}, z :{array[point1][2]:.3f} dan titik dengan koordinat x :{array[point2][0]:.3f}, y :{array[point2][1]:.3f}, z :{array[point2][2]:.3f} dengan jarak sebesar {min:.3f}")
    print(f"Waktu yang diperlukan untuk algoritma bruteforce adalah {(end-start) * 1000:.3f} ms")
    print(f"Jumlah operasi euclidean distance algoritma brute force adalah {count}")
    return point1+1, point2+1

# Variabel untuk menghitung operasi euclidean distance
count = 0
def distance(point1, point2, dimensi):
    global count
    jarak = 0
    for i in range(dimensi):
        jarak += (point2[i] - point1[i]) ** 2
    count += 1
    return math.sqrt(jarak)


# Function to check whether point1 and point2 needs to be checked further
def needToCheck(point1, point2, minimum, dimensi):
    proses = True
    jarak = 0
    for i in range(dimensi):
        jarak += (point2[i] - point1[i]) ** 2
        if (jarak > minimum**2):
            proses = False
            break
    return proses

def divideAndConquer(points, dimensi):
    # Mengurutkan array dari x axis menaik
    quickSort(points, 0, len(points) - 1)
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

        # Mencari pasangan titik yang nilai distancenya lebih kecil dari minLeft atau minRight jika ada
        for i in range(len(midPoint)):
            for j in range(i+1, len(midPoint)):
                if (dimensi > 3):
                    if (needToCheck(midPoint[i], midPoint[j], min, dimensi)):
                        minMid = distance(midPoint[i], midPoint[j], dimensi)
                        if (minMid < min):
                            min = minMid
                            array = [midPoint[i], midPoint[j]]
                else:
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


# Searching index of the point in array of points
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
