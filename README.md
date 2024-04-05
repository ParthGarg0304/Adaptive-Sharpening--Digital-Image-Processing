# Adaptive-Sharpening--Digital-Image-Processing


AIM

To enhance the sharpness and detail of the input image using adaptive sharpening, while avoiding noise and artifacts.

ALGORITHM
1.	Load the Image: Read the input image from a specified file path into memory.
2.	Grayscale Conversion: Convert the original image to a grayscale image to facilitate edge detection.
3.	Gaussian Blurring: Apply a Gaussian blur to the grayscale image to reduce noise and detail, which aids in the detection of significant edges.
4.	Edge Detection: Perform Canny edge detection on the blurred grayscale image to identify edges.
5.	Edge Dilatation: Dilate the edges detected by the Canny algorithm to broaden the impact of sharpening around the edges.
6.	Sharpening Kernel Creation: Define a sharpening kernel (also known as an unsharp mask) to enhance edges in the image.
7.	Color Channel Processing: For each color channel in the original image (Red, Green, and Blue), apply the following steps:
8.	Channel Sharpening: Apply the sharpening kernel to the current channel to create a sharpened version.
9.	Edge-based Blending: Combine the sharpened channel with the original channel based on the dilated edge map, applying the sharpening only where edges are detected.
10.	Save the Sharpened Image: Write the final sharpened image to a file on the disk.
11.	Display the Image: Display the final sharpened image in a window.
