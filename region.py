# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 02:14:38 2024

@author: Asus GK
"""

import cv2  #Mengimpor modul cv2 dari OpenCV
import numpy as np  #numpy digunakan untuk operasi matriks dan array
from matplotlib import pyplot as plt  #Mengimpor submodule dari Matplotlib untuk visualisasi data

def region_filling(image):  #Mengisi area yang terhubung dalam sebuah citra biner 
    img = image.copy()  # Membuat salinan citra untuk hasil
    
    # Menggunakan flood fill untuk mengisi area kosong
    h, w = img.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    
    start_point = (0, 0)  #Menentukan titik awal untuk flood fill
    
    cv2.floodFill(img, mask, start_point, 255)   # Melakukan flood fill

    return img  #Mengembalikan sebuah citra sebagai hasil dari suatu proses

img = cv2.imread("C:/Users/Asus GK/Downloads/apel2.jpg", 0)  # Membaca citra

_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)  # Mengubah citra ke biner

filled_img = region_filling(binary_img)  # Melakukan region filling

# Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Region Filled Image']
images = [img, binary_img, filled_img]

for i in range(3):  #Melakukan loop 3 kali
    plt.subplot(1, 3, i + 1)   #Membuat subplot
    plt.imshow(images[i], 'gray')  #Menampilkan gambar pada indeks i dalam skala abu-abu
    plt.title(titles[i])  #Menetapkan judul subplot
    plt.xticks([]), plt.yticks([])  #Menyembunyikan tanda centang sumbu x dan y, dengan menyediakan daftar kosong

plt.show()  #Menampilkan visualisasi data
