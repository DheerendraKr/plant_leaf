import numpy as np
import cv2
import Background_subtractor

#path="D:/python/final_/Leaves/plant1/1.jpg"
path="l2.jpg"
img=cv2.imread(path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(640,480))

img1=img
img2=img
img3=img
img4=img
img5=img
img6=img
img7=img
img8=img

print(bin(255))

for i in range(640):
    for j in range(480):
        val = int(img[i][j])

        val=bin(val)
        val=str(val)
        #print(val.__len__())

        #print(val[9])

        img1[i][j] = int(val[2])
        img2[i][j] = int(val[3])
        img3[i][j] = int(val[4])
        img4[i][j] = val[5]
        img5[i][j] = val[6]
        img6[i][j] = val[7]
        img7[i][j] = val[8]

        if val[2:-1].__len__() < 7:
            img8[i][j] = 0
        else:
            img8[i][j]=val[9]

cv2.imshow("original_image",img)
cv2.imshow("bit_plane1",img1)
cv2.imshow("bit_plane2",img2)
cv2.imshow("bit_plane3",img3)
cv2.imshow("bit_plane4",img4)
cv2.imshow("bit_plane5",img5)
cv2.imshow("bit_plane6",img6)
cv2.imshow("bit_plane7",img7)
cv2.imshow("bit_plane8",img8)

cv2.waitKey(0)
cv2.destroyAllWindows()
