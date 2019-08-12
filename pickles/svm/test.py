import pickle as pi
import numpy as np

file=open("svm_plant_feature_set.pickle","rb")
#file=open("plant_1.pickle","rb")
data=pi.load(file)
print(data[1])
print(data[1].__len__())
print("*"*100)
print(data[3])
print(data[3][:].__len__())
dl=[]
#dl.append(data[0][1200][:-1])
#print(dl)
#print(data[0].__len__())
#for i in data[0]:
	#print(i)