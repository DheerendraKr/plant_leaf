import pickle
import numpy as np

feature_set=[]
for i in range(1,51,1):
	file=open("plant_27_leaf_"+str(i)+".pickle","rb")
	data=pickle.load(file)
	feature_set.append(data)

feature_set=np.array(feature_set)
with open("plant_27.pickle","wb") as f:
	pickle.dump([feature_set],f)
