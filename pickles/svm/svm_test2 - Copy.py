# importing necessary libraries
#from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pickle
from sklearn.svm import SVC
 
# loading the iris dataset
#iris = datasets.load_iris()

#file=open("svm_plant_feature_set.pickle","rb")
file=open("svm_plant_feature_set.pickle","rb")
data=pickle.load(file)
 
# X -> features, y -> label
#X = iris.data
#y = iris.target
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

#print(x_train[2])
print("*"*60)

#print(y_train[2])
print("*"*60)

#print(x_test[2])
print("*"*60)

#print(y_test[2])
print("*"*60)

# dividing X, y into train and test data
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
 
# training a linear SVM classifier
svm_model_linear = SVC(kernel = 'linear', C = 1).fit(x_train, y_train)
svm_predictions = svm_model_linear.predict(x_test)
 
# model accuracy for X_test  
accuracy = svm_model_linear.score(x_test, y_test)
print(accuracy)
print("*"*60)

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(svm_model_linear, open(filename, 'wb'))