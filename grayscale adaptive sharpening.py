import cv2
import numpy as np

# Load the image
img = cv2.imread(r'D:\parth\personal\SRM\SEM 4\DIP\Impathon\Impathon image.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Edge detection
edges = cv2.Canny(blurred, 300, 600)

# Dilate the edge mask to make the sharpening effect a bit broader on the edges
kernel = np.ones((3,3), np.uint8)
edges_dilated = cv2.dilate(edges, kernel, iterations=1)

# Create the sharpening kernel
sharpening_kernel = np.array([[-1,-1,-1], 
                              [-1, 9,-1],
                              [-1,-1,-1]])

# Sharpen the image using the sharpening kernel
sharpened = cv2.filter2D(gray, -1, sharpening_kernel)

# Convert edges to a binary mask
mask = edges_dilated > 0

# Create a final image that applies the sharpened image only over the edges
final = gray.copy()
final[mask] = sharpened[mask]

# Save or display the final image
cv2.imwrite(r'D:\parth\personal\SRM\SEM 4\DIP\Impathon\bw_sharpened_image.JPG', final)
# If you want to display the image, uncomment the lines below
cv2.imshow('Sharpened Image', final)
cv2.waitKey(0)
cv2.destroyAllWindows()
