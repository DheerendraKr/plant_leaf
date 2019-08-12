import numpy as np
import cv2
from matplotlib import pyplot

class Countblackpixels:
    def countBlackPixels(self,img):
        width,height=img.shape[::-1]
        #print(height)
        #print(width)
        nu=cv2.countNonZero(img)
        #print(nu)
        #print(height*width)

        black=height*width-nu

        return black
