import cv2
import numpy as np

gambar= [
         cv2.imread("C:/Users/Asus GK/Downloads/capraria.png"),
         cv2.imread("C:/Users/Asus GK/Downloads/antigua.png")]

def getCenterofLine(object1, object2, x = 0, y = 0):
    offset = (int(object1[0]/2) + int(object2[0]/2) + x,
              int(object1[1]/2) + int(object2[1]/2) + y)
    return offset

closeIterations = [20, 1]
openIterations = [10, 1]
kernelOpen = np.ones((5,5), np.uint8)
kernelClose = np.ones((5,5), np.uint8)
pusat = []

for i in range(len(gambar)):
    gambar[i] = cv2.resize(gambar[i], (640, 480))
    abu = cv2.cvtColor(gambar[i], cv2.COLOR_BGR2GRAY)
    _, biner = cv2.threshold(abu, 127, 255, cv2.THRESH_BINARY)

    # Melakukan operasi closing dan opening pada citra
    closing = cv2.morphologyEx(biner, cv2.MORPH_CLOSE, kernelClose, iterations = closeIterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen, iterations = openIterations[i])

    # Segmentasi citra
    segmen = cv2.Canny(opening, 200, 200)
    contours, _ = cv2.findContours(segmen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    segmen = cv2.cvtColor(segmen, cv2.COLOR_GRAY2RGB)

    #Segmentasi, clustering, pemberian label, dan menghitung parameter pada citra

    for j in range(len(contours)):
        # Segmentasi, clustering dan pemberian label
        moments = cv2.moments(contours[j])
        pusat.append((int(moments['m10']/moments['m00']), int(moments['m01'] / moments['m00']))) # Mencari centroid
        cv2.circle(gambar[i], pusat[-1], 1, (0, 0, 255), -1) # Menggambar bulat pada centroid
        cv2.putText(gambar[i], str(j+1), pusat[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (255, 0, 0), 1) # Memberi nomor pada centroid
print(pusat)
pixelDistance = cv2.norm(pusat[0], pusat[1], cv2.NORM_L2)
kmDistance = pixelDistance / 2.098181818181818 # 2.09 px / 1m
cv2.line(gambar[0], pusat[0], pusat[1], (0, 255, 255), 2)
cv2.putText(gambar[0], f'd = {pixelDistance} px', getCenterofLine(pusat[0], pusat[1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255), 1)
cv2.putText(gambar[0], f'd = {kmDistance} m', getCenterofLine(pusat[0], pusat[1], y=-20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255), 1)

pixelDistance = cv2.norm(pusat[3], pusat[9], cv2.NORM_L2)
kmDistance = pixelDistance / 4.628099173553719 # 4.62 px / 1km
cv2.line(gambar[1], pusat[3], pusat[9], (0, 255, 255), 2)
cv2.putText(gambar[1], f'd = {pixelDistance} px', getCenterofLine(pusat[3], pusat[9]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255), 1)
cv2.putText(gambar[1], f'd = {kmDistance} km', getCenterofLine(pusat[3], pusat[9], y=-20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255), 1)


for i in range(len(gambar)):
    cv2.imshow(f'Gambar {i+1}', gambar[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
