# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 02:34:09 2024

@author: Asus GK
"""

import cv2  #Mengimpor modul cv2 dari OpenCV
import numpy as np  #numpy digunakan untuk operasi matriks dan array
from matplotlib import pyplot as plt  #Mengimpor submodule dari Matplotlib untuk visualisasi data

img = cv2.imread("C:/Users/Asus GK/Downloads/apel2.jpg", 0)  #Membaca citra

_, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)  #Mengubah citra ke biner

num_labels, labels_im = cv2.connectedComponents(binary_img)  #Menerapkan connected components

#Menampilkan citra
titles = ['Original Image', 'Binary Image', 'Connected Components']
images = [img, binary_img, labels_im]

for i in range(3):  #Melakukan loop 3 kali
    plt.subplot(1, 3, i + 1)  #Membuat subplot
    plt.imshow(images[i], 'gray')  #Menampilkan gambar pada indeks i dalam skala abu-abu
    plt.title(titles[i])  #Menetapkan judul subplot
    plt.xticks([]), plt.yticks([])  #Menyembunyikan tanda centang sumbu x dan y, dengan menyediakan daftar kosong

plt.show()  #Menampilkan visualisasi data

print(f'Jumlah connected components: {num_labels - 1}')  #Menampilkan jumlah komponen terhubung dan Mengurangi 1 untuk tidak menghitung background
