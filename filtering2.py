# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:18:54 2024

@author: Asus GK
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Memuat gambar
img_color = cv2.imread("C:/Users/Asus GK/Downloads/semangka.webp", 1)
img_gray = cv2.imread("C:/Users/Asus GK/Downloads/semangka.webp", 0)

#Menghitung histogram asli
histr_img = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

#Menerapkan filter gambar
filter_maximum = cv2.dilate(img_gray, np.ones((3, 3), np.uint8))  #Menggunakan operasi dilasi untuk memperbesar area terang pada citra. Kernel berukuran 3x3.
filter_minimum = cv2.erode(img_gray, np.ones((3, 3), np.uint8))   #Menggunakan operasi erosi untuk memperkecil area terang. Kernel berukuran 3x3.
filter_median = cv2.medianBlur(img_gray, 3)  #Menerapkan median blur untuk mengurangi noise dengan mengambil nilai median dari piksel dalam kernel 3x3.
filter_gaussian = cv2.GaussianBlur(img_gray, (3, 3), 0)  #Menerapkan Gaussian blur untuk mengaburkan citra dengan kernel 3x3 dan sigma 0.

#Menghitung histogram filter
histr_maximum = cv2.calcHist([filter_maximum], [0], None, [256], [0, 256])
histr_minimum = cv2.calcHist([filter_minimum], [0], None, [256], [0, 256])
histr_median = cv2.calcHist([filter_median], [0], None, [256], [0, 256])
histr_gaussian = cv2.calcHist([filter_gaussian], [0], None, [256], [0, 256])

titles = ['Original Image', 'Maximum Filter', 'Minimum Filter', 'Median Filter', 'Gaussian Filter']
images = [img_color, filter_maximum, filter_minimum, filter_median, filter_gaussian]
histograms = [histr_img, histr_maximum, histr_minimum, histr_median, histr_gaussian]

plt.figure(figsize=(12, 10))  #Membuat figure baru dengan ukuran 12x10 inci untuk menampung semua subplot.
for i in range(5):
    plt.subplot(5, 2, 2*i+1)  #Membuat subplot untuk menampilkan gambar (1 kolom, 2 kolom, dan subplot ke-i).
    if i == 0:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # Mengonversi dari BGR ke RGB untuk tampilan yang benar
    else:
        plt.imshow(images[i], cmap='gray')
    
    #Menetapkan judul subplot menggunakan nama citra dan menghilangkan sumbu untuk tampilan yang lebih bersih.
    plt.title(titles[i])
    plt.axis('off') 

    plt.subplot(5, 2, 2*i+2)  #Membuat subplot kedua untuk histogram, dengan posisi genap (2, 4, 6, 8, 10).
    plt.plot(histograms[i])  #Menampilkan histogram untuk gambar yang sesuai menggunakan fungsi plot.
    plt.xlim([0, 256])  #Mengatur batas sumbu x dari histogram dari 0 hingga 256.
    #Menetapkan judul histogram sesuai dengan nama citra. Menghilangkan tanda di sumbu x dan y untuk tampilan yang lebih bersih.
    plt.title(f"Histogram of {titles[i]}")
    plt.xticks([]), plt.yticks([])

#Menyesuaikan tata letak subplot agar tidak saling tumpang tindih dan menampilkan gambar serta histogram.
plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()