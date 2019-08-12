from feature_extractor.leaf_image_capture import Capture_image
import numpy
import cv2
class Rgbtogray:
    def rgbToGray(self,img_name):

        gray=cv2.cvtColor(img_name,cv2.COLOR_BGR2GRAY)


        #cv2.imshow('image',gray)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        return gray
