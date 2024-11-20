# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:22:45 2024

@author: Asus GK
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Memuat gambar
img_color = cv2.imread("C:/Users/Asus GK/Downloads/semangka.webp", 1)
img_gray = cv2.imread("C:/Users/Asus GK/Downloads/semangka.webp", 0)

#Operasi pengaburan
blur1 = cv2.blur(img_gray, (3, 3))  #Menggunakan metode averaging untuk mengaburkan gambar dengan kernel 3x3.
blur2 = cv2.GaussianBlur(img_gray, (3, 3), 0)  #Menggunakan Gaussian blur dengan kernel 3x3 dan sigma 0.
median = cv2.medianBlur(img_gray, 3)   #Menggunakan median blur dengan ukuran kernel 3, yang membantu mengurangi noise.
blur3 = cv2.bilateralFilter(img_gray, 9, 75, 75)  #Menggunakan bilateral filter dengan diameter 9, sigmaColor 75, dan sigmaSpace 75, yang menjaga tepi sambil meredam noise.

#Plotting gambar dan histogram
def plot_image_and_histogram(image, title, is_color=False):
    plt.figure(figsize=(12, 5))  #Membuat sebuah figure baru dengan ukuran 12x5 inci untuk visualisasi.
    plt.subplot(1, 2, 1)  #Membuat subplot pertama (1 baris, 2 kolom, subplot ke-1) untuk menampilkan gambar.
    if is_color:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
        plt.imshow(image)  #Memeriksa apakah citra berwarna atau grayscale.
    else:
        plt.imshow(image, cmap='gray')
    
    #Menetapkan judul subplot menggunakan nama citra dan menghilangkan sumbu untuk tampilan yang lebih bersih.
    plt.title(f'{title} Image', fontsize=14)
    plt.axis('off')  


    plt.subplot(1, 2, 2)  #Membuat subplot kedua untuk menampilkan histogram
    plt.hist(image.ravel(), bins=256, color='blue', alpha=0.7)  #Menghitung dan menampilkan histogram dari citra.
    #Menetapkan judul histogram, label untuk sumbu x (intensitas piksel) dan y (frekuensi), serta menambahkan grid dengan gaya dan transparansi tertentu. Mengatur batas x dari histogram dari 0 hingga 256.
    plt.title(f"Histogram of {title}", fontsize=14)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim([0, 256])
    
    #Menyesuaikan tata letak subplot agar tidak saling tumpang tindih dan menampilkan gambar serta histogram.
    plt.tight_layout()
    plt.show()

#untuk menampilkan gambar asli dan hasil pengaburan dari berbagai teknik yang telah diterapkan, dengan menyertakan judul yang sesuai untuk masing-masing gambar.
plot_image_and_histogram(img_color, "Original", is_color=True)
plot_image_and_histogram(blur1, "Averaging Blur")
plot_image_and_histogram(blur2, "Gaussian Blur")
plot_image_and_histogram(blur3, "Bilateral Blur")
plot_image_and_histogram(median, "Median Blur")

cv2.waitKey(0)
cv2.destroyAllWindows()