# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:03:00 2024

@author: Asus GK
"""

import cv2  #Mengimpor modul cv2 dari OpenCV
import numpy as np  #numpy digunakan untuk operasi matriks dan array
from matplotlib import pyplot as plt  #Mengimpor submodule dari Matplotlib untuk visualisasi data

img = cv2.imread("C:/Users/Asus GK/Downloads/apel2.jpg",0)  #Membaca citra grayscale

kernel = np.ones((3,3),np.uint8)  #Membuat matriks 3x3 yang berisi angka 1, digunakan sebagai elemen struktur untuk operasi morfologi

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel) #Melakukan operasi opening


titles = ['Normal Image', 'opening']  #Membuat judul yang akan ditampilkan

images = [img, opening]  #Membuat list untuk menyimpan kedua citra

cv2.imshow('opening', opening)  #Menampilkan hasil opening
cv2.waitKey(0)  #Menunggu 0 milidetik untuk menekan tombol pada jendela. 
cv2.destroyAllWindows()  #Menutup semua jendela yang terbuka