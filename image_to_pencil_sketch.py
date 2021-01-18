# Converting an image to a pencil sketch

import cv2

# Get the image location and filename
img_location = "C:/Users/alikh/Downloads/"
filename = "puppy.jpg"

# Read in the image
img = cv2.imread(img_location + filename)

# Convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_gray_image = 255 - gray_image

# Blur the image by Gaussian function
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)

# Invert the blur image
inverted_blurred_image = 255 - blurred_image

# Create the pencil sketch image
pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

# Show the image
# cv2.imshow("Original image", img)
# cv2.imshow("Gray image", gray_image)
# cv2.imshow("Inverted gray image", inverted_gray_image)
# cv2.imshow("Blurred gray image", blurred_image)
# cv2.imshow("Inverted blurred gray image", inverted_blurred_image)
cv2.imshow("Pencil sketch image", pencil_sketch_image)

cv2.waitKey(0)
