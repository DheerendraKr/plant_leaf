import pickle
import random
import numpy as np

feature_set=[]
for i in range(1,33,1):
	file=open("plant_"+str(i)+".pickle","rb")
	data=pickle.load(file)
	for j in range(0,50,1):
		d=[]
		d.append(data[0][j][0][:])
		d.append(data[0][j][1][:-1])
		#d.append([i])
		feature_set.append(d)

feature_set=np.array(feature_set)
#random.shuffle(feature_set)
with open("ann_plant_feature.pickle","wb") as f:
	pickle.dump([feature_set],f)

test_size=10

#train_x=list(feature_set[:,0][:-test_size])
#train_y=list(feature_set[:,1][:-test_size])

#test_x=list(feature_set[:,0][-test_size :])
#test_y=list(feature_set[:,1][-test_size :])
train=[]
test=[]
end=40
i=0
while i < (feature_set.__len__()):
	#print(i)
	if i < end:
		#print("tr..........",i)
		train.append(feature_set[i])
		#train_y.append(feature_set[i][1])
		i+=1
	elif (i >= end) & (i < end+test_size):
		#print("te..........",i)
		test.append(feature_set[i]) 
		#test_y.append(feature_set[i][1])
		i+=1
	else:
		#print("cond.....",i)
		end+=50

#train=np.array(train)
random.shuffle(train)
#train_y=np.array(train_y)
#test=np.array(test)
random.shuffle(test)
print(train[1])
train_x=[]
train_y=[]
test_x=[]
test_y=[]
for i in train:
	train_x.append(i[0])
	train_y.append(i[1])
for i in test:
	test_x.append(i[0])
	test_y.append(i[1])
train_x=np.array(train_x)
train_y=np.array(train_y)
test_x=np.array(test_x)
test_y=np.array(test_y)
print(train_x[0].__len__())
print(train_y.__len__())
print(test_x.__len__())
print(test_y[0].__len__())

print(feature_set.__len__())

with open("ann_plant_feature_set.pickle","wb") as f:
	pickle.dump([train_x,train_y,test_x,test_y],f)