import numpy as np
import cv2
import pickle
import Background_subtractor

path="D:/python/final_/Leaves/plant1/1.jpg"
#path="l2.jpg"
img=cv2.imread(path)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(640,480))
retval,blc=cv2.threshold(img,230,255,cv2.THRESH_BINARY)
cv2.imshow("black",blc)
pl1 = blc
pl2 = blc
pl3 = blc
pl4 = blc
pl5 = blc
pl6 = blc
pl7 = blc
pl8 = blc

for i in range(0,480,1):
    for j in range(0,640,1):
        bin_val=np.binary_repr(img[i][j],width=8)
        bin_val=str(bin_val)
        #print(bin_val)
        #print(bin_val[4])
        pl1[i][j]=int(bin_val[0])
        pl2[i][j]=int(bin_val[1])
        pl3[i][j]=int(bin_val[2])
        pl4[i][j]=int(bin_val[3])
        pl5[i][j]=int(bin_val[4])
        pl6[i][j]=int(bin_val[5])
        pl7[i][j]=int(bin_val[6])
        pl8[i][j]=int(bin_val[7])


cv2.imshow("original_image",img)
cv2.imshow("pl1",pl1)

cv2.waitKey(0)
cv2.destroyAllWindows()



