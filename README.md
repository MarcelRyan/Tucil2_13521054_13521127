# Tucil2_13521054_13521127
Disusun untuk memenuhi Tugas Kecil 2 IF2211 Strategi Algoritma <br>
Mencari Pasangan Titik Terdekat 3D dengan Algoritma Divide and Conquer

## General Information
Mencari sepasang titik terdekat dengan Algoritma Divide and Conquer sudah dijelaskan di dalam kuliah. Persoalan tersebut dirumuskan untuk titik pada bidang datar (2D). Pada Tucil 2 kali ini Anda diminta mengembangkan algoritma mencari sepasang titik terdekat pada bidang 3D. Misalkan terdapat n buah titik pada ruang 3D. Setiap titik P di dalam ruang dinyatakan dengan koordinat P = (x, y, z). Carilah sepasang titik yang mempunyai jarak terdekat satu sama lain. Jarak dua buah titk P1 = (x1, y1, z1) dan P2 = (x2, y2, z2) dihitung dengan rumus Euclidean berikut: 

$$d = {\sqrt{{(x1 - x2)}^2 + {(y1 - y2)}^2 + {(z1 - z2)}^2}}$$

Program dibuat dalam dalam Bahasa Python untuk mencari sepasang titik yang jaraknya terdekat datu sama lain dengan menerapkan algoritma divide and conquer untuk penyelesaiannya, dan perbandingannya dengan Algoritma Brute Force.

## How To Run
1. Di terminal (cmd), jalankan:
```shell
run.bat
```
2. Atau double klik pada file `run.bat`

## Tech Stack
### Programming Languange
* Python 3.11.0

### Libraries
* random
* time
* math
* numpy
* sys
* matplotlib.pyplot
* mpl_toolkits.mplot3d
* os

## Project Structure
```bash
.
├── README.md
├── run.bat
│
├── doc
│    │
│    └── Tucil2_13521054_13521127.pdf
│
├── src
│    │
│    ├── closestPoint.py
│    └── visualization.py
│
└── test
     ├── test1.txt
     ├── test2.txt
     ├── test3.txt
     └── test4.txt
     
```

## Credits
This project is implemented by: 
1. Wilson Tansil (13521054)
2. Marcel Ryan Antony (13521127)