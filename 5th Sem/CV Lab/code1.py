import cv2

#Writing a python program to load and display an image using OpenCV functions, suck as imread(),imshow() and waitKey()
#loading the image
image = cv2.imread('./images/tiger.jpg')
#display image
cv2.imshow('Tiger',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Check size of image
print(image.shape)

#Convert image to grayscale image
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray_tiger',gray_image)
cv2.waitKey(0)
cv2.destroyWindows()


#Chck size of the grayscale image
print(gray_image.size)


#Acccess value of the pixel in the image
print(image[0,0])





