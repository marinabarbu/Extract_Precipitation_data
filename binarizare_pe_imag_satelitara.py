from PIL import Image
import numpy as np

img = Image.open("mask_alunu.tif")
imgarray = np.array(img)

print(imgarray.shape)
print(imgarray[:,150,2])

for i in range(imgarray.shape[0]):
    for j in range(imgarray.shape[1]):
        if imgarray[i, j, 0] == 255 and imgarray[i, j, 1] == 0 and imgarray[i, j, 2] == 0:
            imgarray[i ,j ,1] = 255
            imgarray[i, j, 2] = 255
        else:
            imgarray[i, j, 0] = 0
            imgarray[i, j, 1] = 0
            imgarray[i, j, 2] = 0

new_img = Image.fromarray(imgarray, 'RGB')
new_img.save('new_img.png')
imgarray = np.array(new_img)

print(imgarray.shape)


