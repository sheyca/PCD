# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:09:04 2024

@author: Asus GK
"""

import cv2  #Mengimpor modul cv2 dari OpenCV
import numpy as np  #numpy digunakan untuk operasi matriks dan array
from matplotlib import pyplot as plt  #Mengimpor submodule dari Matplotlib untuk visualisasi data

def thinning(image):  
    img = image.copy()  #Membuat salinan citra untuk hasil
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]], np.uint8)  # Struktur elemen untuk operasi thinning

    while True:
        #Menghitung jumlah piksel tetangga
        eroded = cv2.erode(img, kernel)
        temp = cv2.dilate(eroded, kernel)
        temp = cv2.subtract(img, temp)
        
        img = eroded.copy()
        img = cv2.subtract(img, temp)

        #Jika tidak ada perubahan, keluar dari loop
        if cv2.countNonZero(temp) == 0:
            break

    return img

img = cv2.imread("C:/Users/Asus GK/Downloads/apel2.jpg", 0)  #Membaca citra

_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)  #Mengubah citra ke biner

thinned_img = thinning(binary_img)  #Melakukan thinning

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Thinned Image']
images = [img, binary_img, thinned_img]

for i in range(3):  #Melakukan loop 3 kali
    plt.subplot(1, 3, i + 1)  #Membuat subplot
    plt.imshow(images[i], 'gray')  #Menampilkan gambar pada indeks i dalam skala abu-abu
    plt.title(titles[i])  #Menetapkan judul subplot
    plt.xticks([]), plt.yticks([])  #Menyembunyikan tanda centang sumbu x dan y, dengan menyediakan daftar kosong

plt.show()  #Menampilkan visualisasi data
