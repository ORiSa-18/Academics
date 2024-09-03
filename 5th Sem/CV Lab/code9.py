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
cv2.waitKey(0)
cv2.destroyAllWindows()
