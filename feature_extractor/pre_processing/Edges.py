import numpy as np
import cv2
from feature_extractor.pre_processing.Graytobin import Graytobin
class Edges:
    def detectEdges(self,img_name):

        retval,threshold=cv2.threshold(img_name,250,255,cv2.THRESH_BINARY)
        #edge=cv2.Canny(threshold,100,230,5)
        edge=cv2.Canny(threshold,250,250)
        #edge=Graytobin().grayToBinary(edge)
        #edge=(255-edge)
        edge=cv2.bitwise_not(edge)
        #cv2.imshow('edge',edge)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        return edge
