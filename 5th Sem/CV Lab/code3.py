# creating neagtive image
import cv2

# importing image
image = cv2.imread("Images/tiger.jpg")

# creating grayscale image
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# creating negative image
image_negative = cv2.bitwise_not(image_gray)

# combine to compare the images
result = cv2.hconcat(image,image_negative)

cv2.imshow("negative image",image_negative)
cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
