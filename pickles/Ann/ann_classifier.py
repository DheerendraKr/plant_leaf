from __future__ import print_function
from keras.models import load_model
import numpy as np
import argparse
import cv2
import pickle

file=open("ann_plant_feature_set.pickle","rb")
data=pickle.load(file)

test=data[2]
print(test[1].__len__())

print("[INFO] loading network architecture and weights...")
model = load_model("ann_classifier")
count=0
for feature in test:
	feature = np.array([feature])
	probs = model.predict(feature)[0]
	#print(probs)
	prediction = probs.argmax(axis=0)

	print(prediction)
	print(count)
	count+=1

