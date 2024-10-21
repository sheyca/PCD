# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:37:29 2024

@author: Asus GK
"""

import cv2
import numpy as np

def detect_edges(image, methods):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = []

    for method in methods:
        if method == 'sobel':
            sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
            edge = cv2.magnitude(sobelx, sobely)
        elif method == 'prewitt':
            kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
            kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
            edge = cv2.filter2D(gray, -1, kernelx) + cv2.filter2D(gray, -1, kernely)
        elif method == 'canny':
            edge = cv2.Canny(gray, 100, 200)  # Adjust thresholds as needed
        elif method == 'zero_crossing':
            laplacian = cv2.Laplacian(gray, cv2.CV_64F)

            # Corrected zero-crossing detection (avoiding out-of-bounds access)
            rows, cols = laplacian.shape
            edge = np.zeros_like(laplacian)
            edge[:-1, :] = np.where((laplacian[:-1, :] > 0) & (laplacian[1:, :] < 0), 255, 0)  # Check only valid rows
            edge[-1, :] = 0  # Handle last row separately (no comparison with next row)

        elif method == 'laplacian':
            edge = cv2.Laplacian(gray, cv2.CV_64F)
        elif method == 'robert':
            kernelx = np.array([[0, 1], [-1, 0]])
            kernely = np.array([[1, 0], [0, -1]])
            edge = cv2.filter2D(gray, -1, kernelx) + cv2.filter2D(gray, -1, kernely)
        else:
            raise ValueError(f"Unknown method: {method}")

        edges.append(edge)

    return edges

# Example usage (replace 'your_image.jpg' with your image path):
img = cv2.imread("C:/Users/Asus GK/Downloads/semangka.webp")
methods = ['sobel', 'prewitt', 'canny', 'zero_crossing', 'laplacian', 'robert']
edges = detect_edges(img, methods)

# Display the original image
cv2.imshow("Original Image", img)

# Display edge-detected images
for i, edge in enumerate(edges):
    cv2.imshow(f"Method: {methods[i]}", edge)

cv2.waitKey(0)
cv2.destroyAllWindows()