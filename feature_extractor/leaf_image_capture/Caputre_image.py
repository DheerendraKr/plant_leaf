import cv2
class Capture_image:
    'takes input the image name'
    #def __init__(self):

    def imageName(self):
        img=str(input("Enter name of image:\n").split(' ')[0])
        mode=Capture_image().capMode()
        img_path="D:/python/final_/images/"+mode+"/"+img
        img_name=cv2.imread(img_path,cv2.IMREAD_COLOR)

        #removing background
        #fgbg=cv2.createBackgroundSubtractorMOG2()
        #fgmask=fgbg.apply(img_name)
        #cv2.imshow('ima',fgmask)

        #resizing the image
        img_name=cv2.resize(img_name,(500,400))

        return img_name



    def capMode(self):
        mode=str(input("input mode \n").split(' ')[0])
        #if mode==str("training") | mode==str("testing"):
            #return mode
        #else:
            #print("Please select correct mode!")
            #exit(0)
        return mode
