from keras.models import Sequential
from keras.layers import Activation
from keras.layers import Dense
from keras import optimizers
from keras.optimizers import SGD
import numpy as np
import os
import pickle

pickle_in=open("ann_plant_feature_set.pickle","rb")
data=pickle.load(pickle_in)
#print("data:",data)
train_x=data[0]
train_y=data[1]

test_x=data[2]
model = Sequential()
model.add(Dense(768, input_dim=24, init="uniform",
    activation="relu"))
model.add(Dense(32, activation="relu", kernel_initializer="uniform"))
model.add(Dense(32))
model.add(Activation("softmax"))

print("[INFO] compiling model...")
sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss="binary_crossentropy", optimizer=sgd,metrics=["accuracy"])
model.fit(train_x, train_y, batch_size = 20, nb_epoch = 50)
print("[INFO] evaluating on testing set...")
(loss, accuracy) = model.evaluate(test_x, test_y,
    batch_size=128, verbose=1)
print("[INFO] loss={:.4f}, accuracy: {:.4f}%".format(loss,
    accuracy * 100))
print("[INFO] dumping architecture and weights to file...")
model.save("ann_classifier")