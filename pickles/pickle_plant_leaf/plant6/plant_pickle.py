import pickle
import numpy as np

feature_set=[]
for i in range(1,51,1):
	file=open("plant_6_leaf_"+str(i)+".pickle","rb")
	data=pickle.load(file)
	feature_set.append(data[0][1])

feature_set=np.array(feature_set)
with open("plant_6.pickle","wb") as f:
	pickle.dump([feature_set],f)
