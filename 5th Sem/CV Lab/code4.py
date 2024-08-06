# generate log transormation

import cv2
import numpy as np

# Load the image
image = cv2.imread("Images/tiger.jpg")

#generating grayscale
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# setting constant
c = 40
image_log = c * np.log(1 + image_gray)
image_log = np.array(image_log, dtype = np.uint8)
# showing result
cv2.imshow("logTransform",image_log)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
