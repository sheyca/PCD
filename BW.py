# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:50:29 2024

@author: Asus GK
"""

import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img = cv2.imread("C:/Users/Asus GK/Downloads/alam.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, BW) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

print("Original = ", img.shape)
print("Gray = ", gray.shape)
print("BW = ", BW.shape)
print(BW)
cv2.imwrite("Hasil.png", BW)

cv2.waitKey(0)
cv2.destroyAllWindows()