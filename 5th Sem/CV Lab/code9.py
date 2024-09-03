import cv2

# Load image
img = cv2.imread("Images/ambigram.jpeg")

# Get original dimensions
height, width = img.shape[:2]

# Resize image
new_height, new_width = int(height / 4), int(width / 4)
img = cv2.resize(img, (new_width, new_height))

# Generate rotation matrix
m = cv2.getRotationMatrix2D((new_width / 2, new_height / 2), 180, 1)

# Apply rotation to image
rotated_image = cv2.warpAffine(img, m, (new_width, new_height))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated_image)

# shrink image
img_shrink = cv2.resize(img,(250,250),interpolation=cv2.INTER_AREA)
cv2.imshow('Shrink',img_shrink)
# enlarge image
img_enlarge = cv2.resize(img_shrink,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow("enlarged",img_enlarge)

# translate image
m = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,m,(width,height))
dst = cv2.resize(dst,((int)(height/4),(int)(width/4)))
cv2.imshow("translate",dst)

# Get original dimensions
height, width = img.shape[:2]
# shear an image
m=np.float32([[1,0.5,0],[0,1,0],[0,0,1]])
img_shear = cv2.warpPerspective(img,m,(int(width*1.5),int(height*1.5)))
img_shear = cv2.resize(img_shear,((int)(height/4),(int)(width/4)))
cv2.imshow("shear",img_shear)

cv2.waitKey(0)
cv2.destroyAllWindows()


