from feature_extractor.pre_processing.Countblackpixels import Countblackpixels
from feature_extractor.pre_processing.Edges import Edges
import cv2
class Perimeter:
    def perimeter(self,img):
        #edge=Edges().detectEdges(img)
        #cv2.imshow('image',edge)

        val=Countblackpixels().countBlackPixels(img)
        #print(val)
        return val
