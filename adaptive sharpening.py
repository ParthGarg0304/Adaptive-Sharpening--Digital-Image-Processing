import cv2
import numpy as np

# Load the image
img = cv2.imread(r'D:\parth\personal\SRM\SEM 4\DIP\Impathon\Impathon image.jpg')

# Convert to grayscale for edge detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Edge detection on the blurred image
edges = cv2.Canny(blurred, 300, 600)

# Dilate the edge mask to make the sharpening effect a bit broader on the edges
kernel = np.ones((3,3), np.uint8)
edges_dilated = cv2.dilate(edges, kernel, iterations=1)

# Create the sharpening kernel
sharpening_kernel = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])

# Initialize the final color sharpened image
sharpened_color_img = img.copy()

# Apply the sharpening kernel to each color channel
for i in range(3):  # loop through the color channels
    channel = img[:, :, i]
    sharpened_channel = cv2.filter2D(channel, -1, sharpening_kernel)
    # Use the edges to blend the sharpened channel with the original channel
    sharpened_color_img[:, :, i] = np.where(edges_dilated, sharpened_channel, channel)

# Save the sharpened image
cv2.imwrite(r'D:\parth\personal\SRM\SEM 4\DIP\Impathon\color_sharpened_image.JPG', sharpened_color_img)

# If you want to display the image, uncomment the lines below
cv2.imshow('Color Sharpened Image', sharpened_color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
