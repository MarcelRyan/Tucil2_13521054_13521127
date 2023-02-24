import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import math

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
array_of_points = []
array_distance = []
# for i in range(16):
#     x_axes = random.randint(0, 10)
#     y_axes = random.randint(0, 10)
#     z_axes = random.randint(0, 10)
#     array_of_points.append([x_axes, y_axes, z_axes])

# for i in range(0, 16, 2):
#     jarak = 0
#     jarak += (array_of_points[i+1][0] - array_of_points[i][0]) ** 2 + (array_of_points[i+1][1] - array_of_points[i][1]) ** 2 + (array_of_points[i+1][2] - array_of_points[i][2]) ** 2
#     print(math.sqrt(jarak))
#     array_distance.append(math.sqrt(jarak))

# min = 10000000
# idx_min = 0
# for i in range(len(array_distance)):
#     if (min > array_distance[i]):
#         min = array_distance[i]
#         idx_min = i

# for i in range(len(array_of_points)):
#     if (i == idx_min * 2 or i == idx_min * 2 + 1):
#         ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "red")
#     else:
#         ax.scatter(array_of_points[i][0], array_of_points[i][1], array_of_points[i][2], color = "blue")


# plt.plot([array_of_points[idx_min*2][0] ,array_of_points[idx_min*2+1][0]] , [array_of_points[idx_min*2][1], array_of_points[idx_min*2+1][1]], [array_of_points[idx_min*2][2], array_of_points[idx_min*2+1][2]], color = 'black',  linestyle = '-')
# plt.ioff()
# plt.show()