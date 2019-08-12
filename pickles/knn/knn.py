import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as pd
import pickle
import random

#df=pd.read_csv('breast_cancer.txt')
#df.replace('?',-99999,inplace=True)
#df.drop(['id'],1,inplace=True)

#x=np.array(df.drop(['class'],1))
#y=np.array(df['class'])

#x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)

file=open("knn_plant_feature_set.pickle","rb")
#file=open("knn_plant_feature_set.pickle","rb")
data=pickle.load(file)
x_train=[]
for i in data[0]:
	x_train.append(i[:-1])
#print(x_train)
print("*"*60)
#random.shuffle(x_train)
y_train=[]
for i in data[0]:
	y_train.append(i[-1])
#print(y_train)
print("*"*60)
#random.shuffle(y_train)
x_test=[]
for i in data[1]:
	x_test.append(i[:-1])
#print(x_test)
print("*"*60)
#random.shuffle(x_test)
y_test=[]
for i in data[1]:
	y_test.append(i[-1])
#print(y_test)
print("*"*60)
#random.shuffle(y_test)


clf=neighbors.KNeighborsClassifier()
clf.fit(x_train,y_train)

accuracy=clf.score(x_test,y_test)
print(accuracy)

#exm_meas=np.array([5,2,1,1,4,3,5,2,1])
#exm_meas=exm_meas.reshape(1,-1)

#exm_meas=np.array([5,2,1,1,4,3,5,2,1],[5,2,1,1,4,1,2,2,1])
#exm_meas=exm_meas.reshape(2,-1)

#prediction=clf.predict(exm_meas)
#print(prediction)