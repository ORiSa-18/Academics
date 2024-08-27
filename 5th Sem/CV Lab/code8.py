# edge detection using sobel operator and Canny edge detector
import cv2
# load image
img = cv2.imread("Images/dhoni.jpg")
# convert to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# apply gaussian blur to remove noise
img_blur = cv2.GaussianBlur(img_gray,(5,5),0)
# apply sobel operator
sobelx = cv2.Sobel(img_blur,cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(img_blur,cv2.CV_8U,0,1,ksize=3)
# combine edges detected in x an y direction
edges = cv2.bitwise_or(sobelx,sobely)
# canny edge detector
edge = cv2.Canny(edges,50,800)
img,edge,edges = cv2.resize(img,(871,490)),cv2.resize(edge,(871,490)),cv2.resize(edges,(871,490))
cv2.imshow("Orignal",img)
cv2.imshow("Sobel",edges)
cv2.imshow("Canny",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
