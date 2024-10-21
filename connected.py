# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:55:44 2024

@author: Asus GK
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def thinning(img):
  # Struktur elemen untuk operasi thinning
  kernel = np.array([[1, 1, 1],
                     [1, 0, 1],
                     [1, 1, 1]], np.uint8)

  # Iterasi thinning
  iterations = 0
  changed = True
  while changed and iterations < 20:
    iterations += 1
    changed = False
    
    # Menghitung jumlah piksel tetangga
    eroded = cv2.erode(img, kernel)
    temp = cv2.dilate(eroded, kernel)
    temp = cv2.subtract(img, temp)
  
    # Tahap 1: Penghapusan cabang tunggal
    deleted1 = cv2.bitwise_and(temp, cv2.bitwise_not(cv2.bitwise_and(
        cv2.bitwise_leftShift(temp, 1, cv2.BORDER_CONSTANT), 
        cv2.bitwise_rightShift(temp, 1, cv2.BORDER_CONSTANT)
    )))
    img = cv2.subtract(img, deleted1)
  
    # Tahap 2: Penghapusan diagonal
    deleted2 = cv2.bitwise_and(temp, cv2.bitwise_not(cv2.bitwise_and(
        cv2.bitwise_leftShift(temp, 1, cv2.BORDER_CONSTANT), 
        cv2.bitwise_rightShift(1, cv2.BORDER_CONSTANT)
    )))
    img = cv2.subtract(img, deleted2)
    
    changed =cv2.countNonZero(temp) > 0

    # Iterasi maksimum untuk mencegah loop tak terhingga
    if iterations >= 20:
      print("Iterasi maksimum tercapai!")

  return img

# Membaca citra
img = cv2.imread("C:/Users/Asus GK/Downloads/apel2.jpg",0)

# Mengubah citra ke biner
_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Melakukan thinning
thinned_img = thinning(binary_img.copy())

# Menampilkan citra
titles = ['Citra Asli', 'Citra Biner', 'Citra Setelah Penipisan']
images = [img, binary_img, thinned_img]

for i in range(3):
  plt.subplot(1, 3, i + 1)
  plt.imshow(images[i], 'gray')
  plt.title(titles[i])
  plt.xticks([]), plt.yticks([])

plt.show