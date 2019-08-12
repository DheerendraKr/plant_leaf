import pickle
import random
import numpy as np

feature_set=[]
for i in range(1,33,1):
	file=open("plant_"+str(i)+".pickle","rb")
	data=pickle.load(file)
	for j in range(0,50,1):
		data[0][j][0].append(i)
		feature_set.append(data[0][j][0])

feature_set=np.array(feature_set)
#random.shuffle(feature_set)
with open("svm_plant_feature.pickle","wb") as f:
	pickle.dump([feature_set],f)

test_size=10

#train_x=list(feature_set[:,0][:-test_size])
#train_y=list(feature_set[:,1][:-test_size])

#test_x=list(feature_set[:,0][-test_size :])
#test_y=list(feature_set[:,1][-test_size :])
train_x=[]
#train_y=[]
test_x=[]
#test_y=[]
end=40
i=0
while i < (feature_set.__len__()):
	#print(i)
	if i < end:
		#print("tr..........",i)
		train_x.append(feature_set[i])
		#train_y.append(feature_set[i][1])
		i+=1
	elif (i >= end) & (i < end+test_size):
		#print("te..........",i)
		test_x.append(feature_set[i]) 
		#test_y.append(feature_set[i][1])
		i+=1
	else:
		#print("cond.....",i)
		end+=50

train_x=np.array(train_x)
random.shuffle(train_x)
#train_y=np.array(train_y)
test_x=np.array(test_x)
random.shuffle(test_x)
#test_y=np.array(test_y)
#print(train_x[1])
print(train_x.__len__())
#print(train_y.__len__())
print(test_x.__len__())
#print(test_y.__len__())

print(feature_set.__len__())

with open("svm_plant_feature_set.pickle","wb") as f:
	pickle.dump([train_x,test_x],f)