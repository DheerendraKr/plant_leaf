import cv2
import numpy as np

class Graytobin:
    def grayToBinary(self,img_name):

        retval,threshold=cv2.threshold(img_name,230,255,cv2.THRESH_BINARY)
        #cv2.imshow('threshold',threshold)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()


        return threshold
