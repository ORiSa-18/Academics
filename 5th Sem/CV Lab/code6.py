import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading image
image = cv2.imread("Images/low_contrast.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Setting grid size
plt.figure(figsize=(20, 20))

# Plotting original image
plt.subplot(221)
plt.title("Original")
plt.imshow(image)

# Plotting histogram for the image
image_histogram = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
plt.subplot(222)
plt.title("Histogram1")
plt.plot(image_histogram)

# Plotting using ravel function
plt.subplot(223)
plt.hist(image_gray.ravel(), 256, [0, 256])
plt.title("Histogram2")

# Applying histogram equalization
image_final = cv2.equalizeHist(image_gray)

# Displaying the equalized image
plt.subplot(224)
plt.title("Equalized Image")
plt.imshow(image_final, cmap='gray')

plt.show()

# Displaying images using OpenCV
cv2.imshow("Original Image", image)
cv2.imshow("Histogram Equalization", image_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
