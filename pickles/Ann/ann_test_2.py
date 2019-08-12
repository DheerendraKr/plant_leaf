import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix

file=open("ann_plant_feature_set.pickle","rb")
data=pickle.load(file)


X_train=data[0]
y_train=data[1]
X_test=data[2]
y_test=data[3]

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 768, init = 'uniform', activation = 'relu', input_dim = 24))
#classifier.add(Dense(output_dim = 32, init = 'uniform', activation = 'relu', input_dim = 24))
# Adding the second hidden layer
classifier.add(Dense(output_dim = 32, init = 'uniform', activation = 'relu'))
# Adding the output layer
classifier.add(Dense(output_dim = 32, init = 'uniform', activation = 'softmax'))
#classifier.add(Dense(output_dim = 32, init = 'uniform', activation = 'sigmoid'))

# Compiling Neural Network
#classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting our model 
#classifier.fit(X_train, y_train, batch_size = 30, nb_epoch = 100)
classifier.fit(X_train, y_train, batch_size = 20, nb_epoch = 50)


# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Creating the Confusion Matrix
#cm = confusion_matrix(y_test, y_pred)

#print(cm)

scores = classifier.evaluate(X_test,y_test)
print("\nAccuracy: %.2f%%" % (scores[1]*100))
