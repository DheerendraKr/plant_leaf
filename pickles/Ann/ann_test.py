# Importing libraries
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy
import pandas as pd
import pickle

file=open("ann_plant_feature_set.pickle","rb")
data=pickle.load(file)
# Import training dataset
#training_dataset = pd.read_csv('iris_training.csv', names=COLUMN_NAMES, header=0)
#train_x = training_dataset.iloc[:, 0:4].values
#train_y = training_dataset.iloc[:, 4].values

train_x=data[0]
train_y=data[1]

# Import testing dataset
#test_dataset = pd.read_csv('iris_test.csv', names=COLUMN_NAMES, header=0)
#test_x = test_dataset.iloc[:, 0:4].values
#test_y = test_dataset.iloc[:, 4].values

test_x=data[2]
test_y=data[3]

# Encoding training dataset
#encoding_train_y = np_utils.to_categorical(train_y)

# Encoding training dataset
#encoding_test_y = np_utils.to_categorical(test_y)

# Creating a model
model = Sequential()
model.add(Dense(768, input_dim=24, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='softmax'))

# Compiling model
#model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# Training a model
model.fit(train_x, train_y, epochs=50, batch_size=30)

# Evaluate the model
scores = model.evaluate(test_x,test_y)
print("\nAccuracy: %.2f%%" % (scores[1]*100))