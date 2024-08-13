import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading image
image = cv2.imread("Images/low_contrast.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image_gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# setting grid size
plt.figure(figsize=(20,20))

#plotting orignal image
plt.subplot(221)
plt.title("Orignal")
plt.imshow(image)

# plotting histogram for the image
image_historgram = cv2.calcHist([image_gray],[0],None,[256],[0,256])
plt.subplot(222)
plt.title("Histogram1")
plt.plot(image_historgram)

# plotting using ravel function
plt.subplot(223)
plt.hist(image_gray.ravel(),256,[0,256])
plt.title("Histogram2")

# Applying histogram equilization
image_final = cv2.equalizeHist(image_gray)


cv2.imshow("Orignal Image",image)
cv2.imshow("Histogram Equilization",image_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
