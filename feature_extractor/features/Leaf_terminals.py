import cv2
import numpy as np


class Leaf_terminals:
    positions=[]
    def draw_circle(self,event,x,y,flags,param):

        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img,(x,y),5,(0,0,0),1)
            self.positions.append((x,y))


    def points(self,img_name,plant_type,leaf_n):
        global img

        plant_type=str(plant_type)
        leaf_n=str(leaf_n)

        img=img_name
        cv2.namedWindow('image_plant_'+plant_type+'_leaf_n'+leaf_n)
        cv2.setMouseCallback('image_plant_'+plant_type+'_leaf_n'+leaf_n,self.draw_circle)

        while(1):

            cv2.imshow('image_plant_'+plant_type+'_leaf_n'+leaf_n,img)

            if self.positions.__len__()==2:
                cv2.destroyWindow('image_plant_'+plant_type+'_leaf_n'+leaf_n)
                break

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                cv2.destroyWindow('image'+plant_type+'leaf_n'+leaf_n)
                break

        cv2.waitKey(1)
        pt=[]
        pt+=self.positions
        self.positions.clear()
        #print(pt)
        return pt

