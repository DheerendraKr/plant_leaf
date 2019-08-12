import pickle
import numpy as np
from sklearn.svm import SVC

#file=open("svm_plant_feature_set.pickle","rb")
file=open("svm_plant_feature_set.pickle","rb")
data=pickle.load(file)

train_data=data[0]
test_data=data[1]
x_train=[]
x_test=[]
y_train=[]
y_test=[]

for i in train_data:
 	x_train.append(i[:-1])
 	y_train.append(i[-1])
for i in test_data:
 	x_test.append(i[:-1])
 	y_test.append(i[-1])


# training a linear SVM classifier
from sklearn.svm import SVC
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(x_train, y_train)
svm_predictions = svm_model_linear.predict(x_test)
 
# model accuracy for X_test  
accuracy = svm_model_linear.score(x_test, y_test)
print(accuracy)
print("*"*60)