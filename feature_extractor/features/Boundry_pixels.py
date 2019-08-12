import numpy as np
import cv2
import math
from feature_extractor.pre_processing.Edges import Edges

class Boundry_pixels:

    def boundryPixels(self,image_name,t):

        image_name=Edges().detectEdges(image_name)

        height,width=image_name.shape[:2]
        set1=list()
        set2=list()
        boundrypixels=list()

        #print(terminals)


        #a1=0
        #a2=0
        #if terminals[0][0]>terminals[1][0]:
        #    a1=terminals[0][0]-terminals[1][0]
        #else:
         #   a1=terminals[1][0]-terminals[0][0]

        #if terminals[0][1]>terminals[1][1]:
         #   a2=terminals[0][1]-terminals[1][1]
        #else:
            #a2=terminals[1][1]-terminals[0][1]

        a1=t[1][0]-t[0][0]
        a2=t[1][1]-t[0][1]

        A=t[1][1]-t[0][1]
        B=t[0][0]-t[1][0]
        C=(t[1][0]*t[0][1])-(t[0][0]*t[1][1])
        D=math.pow((A**2 + B**2),0.5)


        for i in range(height):
            for j in range(width):
                if image_name[i][j]!=255:
                    #d=(A*i + B*j+ C)
                    d=((j-t[0][0])*a2) - ((i-t[0][1])*a1)
                    if d < 0:
                        set1.append((i,j))
                    elif d > 0:
                        set2.append((i,j))

        #print(set1)
        #print(set1.__len__())

        #print(set2)
        #print(set2.__len__())

        #boundrypixels.append(set1)
        #boundrypixels.append(set2)

        #return boundrypixels

        return set1,set2
