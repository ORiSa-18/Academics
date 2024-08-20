import cv2
import numpy as np

# load image
img = cv2.imread("Images/noise.png")
img1 = cv2.imread("Images/foool.jpg")
imgd = cv2.resize(img1,(1068,712))
# kernel matrix
kernel = np.ones((5,5),np.float32)/25

# apply mean filter
img_mean = cv2.filter2D(img,-1,kernel)

# apply median filter
img_median = cv2.medianBlur(img,5)

# sharpen image
img_sharp = cv2.Laplacian(img1,cv2.CV_8U)
img_sharp = cv2.resize(img_sharp,(1068,712))


# Display filtered image
cv2.imshow("Orignal Image",imgd);
cv2.imshow("Orignal Image",img);
cv2.imshow("Mean Filter Image",img_mean);
cv2.imshow("Median Filter",img_median);
cv2.imshow("Laplacian Filter",img_sharp);
cv2.waitKey(0);
cv2.destroyAllWindows();
