import cv2

original_image=cv2.imread("leaf.jpg")
original_image=cv2.resize(original_image,(640,480))
bin=cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
retval,threshold=cv2.threshold(bin,230,255,cv2.THRESH_BINARY)
slice_1=threshold
slice_2=threshold
slice_3=threshold
slice_4=threshold
slice_5=threshold
slice_6=threshold
slice_7=threshold
slice_8=threshold

width,height=bin.shape[::-1]
for i in range(height):
    for j in range(width):
        val=bin[i][j]
        m=255/8
        if 0<= val <= m:
            slice_1[i][j]=1
            slice_2[i][j]=0
            slice_3[i][j]=0
            slice_4[i][j]=0
            slice_5[i][j]=0
            slice_6[i][j]=0
            slice_7[i][j]=0
            slice_8[i][j]=0
        elif m < val <= 2*m:
            slice_1[i][j]=0
            slice_2[i][j]=1
            slice_3[i][j]=0
            slice_4[i][j]=0
            slice_5[i][j]=0
            slice_6[i][j]=0
            slice_7[i][j]=0
            slice_8[i][j]=0
        elif 2*m< val <= 3*m:
            slice_1[i][j]=0
            slice_2[i][j]=0
            slice_3[i][j]=1
            slice_4[i][j]=0
            slice_5[i][j]=0
            slice_6[i][j]=0
            slice_7[i][j]=0
            slice_8[i][j]=0
        elif 3*m< val <= 4*m:
            slice_1[i][j]=0
            slice_2[i][j]=0
            slice_3[i][j]=0
            slice_4[i][j]=1
            slice_5[i][j]=0
            slice_6[i][j]=0
            slice_7[i][j]=0
            slice_8[i][j]=0
        elif 4*m< val <= 5*m:
            slice_1[i][j]=0
            slice_2[i][j]=0
            slice_3[i][j]=0
            slice_4[i][j]=0
            slice_5[i][j]=1
            slice_6[i][j]=0
            slice_7[i][j]=0
            slice_8[i][j]=0
        elif 5*m< val <= 6*m:
            slice_1[i][j]=0
            slice_2[i][j]=0
            slice_3[i][j]=0
            slice_4[i][j]=0
            slice_5[i][j]=0
            slice_6[i][j]=1
            slice_7[i][j]=0
            slice_8[i][j]=0
        elif 6*m< val <= 7*m:
            slice_1[i][j]=0
            slice_2[i][j]=0
            slice_3[i][j]=0
            slice_4[i][j]=0
            slice_5[i][j]=0
            slice_6[i][j]=0
            slice_7[i][j]=1
            slice_8[i][j]=0
        elif 7*m< val <= 8*m:
            slice_1[i][j]=0
            slice_2[i][j]=0
            slice_3[i][j]=0
            slice_4[i][j]=0
            slice_5[i][j]=0
            slice_6[i][j]=0
            slice_7[i][j]=0
            slice_8[i][j]=1


cv2.imshow("slice_1",slice_1)
cv2.imshow("slice_2",slice_2)
cv2.imshow("slice_3",slice_3)
cv2.imshow("slice_4",slice_4)
cv2.imshow("slice_5",slice_5)
cv2.imshow("slice_6",slice_6)
cv2.imshow("slice_7",slice_7)
cv2.imshow("slice_8",slice_8)
cv2.imshow("original_image",original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
