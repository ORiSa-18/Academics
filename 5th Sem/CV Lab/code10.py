import cv2
import numpy as np

# load image
img1 = cv2.imread("Images/image1.jpeg")
img2 = cv2.imread("Images/image2.jpeg")

# convert to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# create SIFT object
sift = cv2.SIFT_create()

# detect SIFT features
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

# create feature matcher
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

# match descriptors
matches = bf.match(descriptors1, descriptors2)

# sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# draw 50 matches
img_matched = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# find accuracy
numKeyPoints1 = len(keypoints1)
numKeyPoints2 = len(keypoints2)
avg = (int) (numKeyPoints1+numKeyPoints2)/2
numMatches = len(matches)
print("Number of Keypoints in image1= ",numKeyPoints1)
print("Number of Keypoints in image2= ",numKeyPoints2)
print("Number of matches= ",numMatches)
print("Accuracy= {:.2f}%".format((numMatches/avg)*100))

#display image
cv2.imshow("Matched Image", img_matched)
cv2.waitKey(0)
cv2.destroyAllWindows()

