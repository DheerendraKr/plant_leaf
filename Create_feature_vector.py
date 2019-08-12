import numpy as np
import random
from collections import Counter
import pickle
import cv2

from feature_extractor.Feature_extractor import Feature_extractor

if __name__=='__main__':


    for i in range(1,50,1):
        feature_set=[]
        output=[]
        for k in range(0,33,1):output.append(0)
        output[i-1]=1

        for j in range(1,2,1):
            path="D:/python/final_/Leaves/plant"+str(i)+"/"+str(j)+".jpg"
            print(path)
            cv2.startWindowThread()
            features=Feature_extractor().featureExtractor(path,i,j)
            print(features)
            features=list(features)
            output=list(output)
            feature_set.append([features,output])
            print(output)
            with open("plant_"+str(i)+"_leaf_"+str(j)+".pickle",'wb') as fi:
                pickle.dump([features,output], fi)
        feature_set=np.array(feature_set)
        with open("plant_"+str(i)+".pickle",'wb') as f:
            pickle.dump([feature_set], f)


    print(feature_set)
