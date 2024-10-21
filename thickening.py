# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:43:06 2024

@author: Asus GK
"""

import cv2  #Mengimpor modul cv2 dari OpenCV
import numpy as np  #numpy digunakan untuk operasi matriks dan array
from matplotlib import pyplot as plt  #Mengimpor submodule dari Matplotlib untuk visualisasi data

def thickening(image):
    img = image.copy()  #Membuat salinan citra untuk hasil
    
    kernel = np.ones((3, 3), np.uint8)  #Struktur elemen untuk operasi thickening
    
    dilated = cv2.dilate(img, kernel, iterations=1)  #Melakukan dilasi beberapa kali
    
    return dilated  #Mengembalikan hasil dari operasi dilasi pada suatu gambar

img = cv2.imread("C:/Users/Asus GK/Downloads/apel2.jpg", 0)  #Membaca citra

_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)  #Mengubah citra ke biner

thickened_img = thickening(binary_img)  #Melakukan thickening

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Thickened Image']
images = [img, binary_img, thickened_img]

for i in range(3):  #Melakukan loop 3 kali
    plt.subplot(1, 3, i + 1)  #Membuat subplot
    plt.imshow(images[i], 'gray')  #Menampilkan gambar pada indeks i dalam skala abu-abu
    plt.title(titles[i])   #Menetapkan judul subplot
    plt.xticks([]), plt.yticks([])  #Menyembunyikan tanda centang sumbu x dan y, dengan menyediakan daftar kosong

plt.show()  #Menampilkan visualisasi data
