import pickle as pi
import numpy as np

file=open("ann_plant_feature_set.pickle","rb")
data=pi.load(file)
print(data[0])
print(data[1])
print(data[0].__len__())
