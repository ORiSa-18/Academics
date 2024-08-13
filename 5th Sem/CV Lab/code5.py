import cv2
import numpy as np

# load image
image = cv2.imread("Images/orange.jpg")

# find dimmensions
rows, columns, channels = image.shape

# create zeros array
converted_image = np.zeros((rows,columns),dtype="uint8")
converted_image = np.asarray(converted_image)
# specify range
min,max = 140,200

white_array = np.full((rows,columns),255,dtype="uint8")
for i in range(rows):
    for j in range(columns):
        if np.any(image[i,j]>min) and np.any(image[i,j]<max):
            converted_image[i,j] = white_array[i,j];
        else:
            converted_image[i,j] = image[i, j,0]

# display the images
cv2.imshow("Orignal Image",image)
cv2.imshow("Sliced Image",converted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
