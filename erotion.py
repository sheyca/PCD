# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:24:59 2024

@author: Asus GK
"""

import cv2  #Mengimpor modul cv2 dari OpenCV
import numpy as np  #numpy digunakan untuk operasi matriks dan array
from matplotlib import pyplot as plt  #Mengimpor submodule dari Matplotlib untuk visualisasi data

img = cv2.imread("C:/Users/Asus GK/Downloads/apel2.jpg",0)  #Membaca citra grayscale

kernel = np.ones((3,3),np.uint8)  #Membuat matriks 3x3 yang berisi angka 1, digunakan sebagai elemen struktur untuk operasi morfologi

erosion = cv2.erode(img,kernel,iterations=1)  #Menerapkan operasi erosi pada citra dengan iterasi sebanyak 1 kali

titles = ['Normal Image', 'Erosion']  #Membuat judul yang akan ditampilkan

images = [img, erosion]  #Membuat list untuk menyimpan kedua citra

cv2.imshow('Erosion', erosion)  #Menampilkan hasil erosi
cv2.waitKey(0)  #Menunggu 0 milidetik untuk menekan tombol pada jendela. 
cv2.destroyAllWindows()  #Menutup semua jendela yang terbuka