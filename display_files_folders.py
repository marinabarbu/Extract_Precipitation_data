import os
import matplotlib.pyplot as plt
from pandas import datetime
import matplotlib.dates as mdates
import datetime
import numpy as np

def parser(x):
    return datetime.datetime.strptime(x, "%Y%m%d")

timeList_Landsat7, timeList_Landsat8, timeList_Sentinel2 = [], [], []

arr = os.listdir('C:\\')
path_Landsat7 = os.listdir('D:\\FACULTATE\\ANUL 4\\SEMESTRUL 2\\1_Licenta\\Licenta\\Imagini Alunu\\Landsat7')

for e in path_Landsat7:
    #print(e[17:25], e[26:34])
    timeList_Landsat7.append(e[17:25])

print()

path_Landsat8 = os.listdir('D:\\FACULTATE\\ANUL 4\\SEMESTRUL 2\\1_Licenta\\Licenta\\Imagini Alunu\\Landsat8')

for e in path_Landsat8:
    #print(e[17:25], e[26:34])
    timeList_Landsat8.append(e[17:25])

print()

path_Sentinel2 = os.listdir('D:\\FACULTATE\\ANUL 4\\SEMESTRUL 2\\1_Licenta\\Licenta\\Imagini Alunu\\Sentinel2 - imagini mari')

for e in path_Sentinel2:
    #print(e[19:27])
    timeList_Sentinel2.append(e[19:27])

print(len(timeList_Landsat7), len(timeList_Landsat8), len(timeList_Sentinel2))
print(timeList_Sentinel2)

new_timeList_Landsat7 = [parser(x) for x in timeList_Landsat7]
print(new_timeList_Landsat7)

X_Landsat7,Y_Landsat7 = np.unique(new_timeList_Landsat7, return_counts=True)
Y_Landsat7 = [1 for x in Y_Landsat7]
plt.subplot(3,1,1)
plt.scatter(X_Landsat7,Y_Landsat7, color='black')
plt.title('Landsat7')


new_timeList_Landsat8 = [parser(x) for x in timeList_Landsat8]
print(new_timeList_Landsat8)

X_Landsat8,Y_Landsat8 = np.unique(new_timeList_Landsat8, return_counts=True)
Y_Landsat8 = [1 for x in Y_Landsat8]
plt.subplot(3,1,2)
plt.scatter(X_Landsat8,Y_Landsat8, color='red')
plt.title('Landsat8')


new_timeList_Sentinel2 = [parser(x) for x in timeList_Sentinel2]
print(new_timeList_Sentinel2)

X_Sentinel2,Y_Sentinel2 = np.unique(new_timeList_Sentinel2, return_counts=True)
Y_Sentinel2 = [1 for x in Y_Sentinel2]
plt.subplot(3,1,3)
plt.scatter(X_Sentinel2,Y_Sentinel2,color='blue')
plt.title('Sentinel2')
plt.ylim(bottom=1)
plt.show()

plt.scatter(X_Landsat7, Y_Landsat7, color='black')
plt.scatter(X_Landsat8, Y_Landsat8, color='red')
plt.scatter(X_Sentinel2, Y_Sentinel2, color='blue')
plt.show()





