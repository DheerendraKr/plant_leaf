import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
import pickle
from collections import Counter
#dont forget this
import pandas as pd
import random
style.use('fivethirtyeight')

def k_nearest_neighbors(data, predict, k=3):
    if len(data) <= k:
        warnings.warn('K is set to a value less than total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance,group])
    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result



file=open("knn_plant_feature_set.pickle","rb")
data=pickle.load(file)



#random.shuffle(data)

test_size = 0.2
train_set = {1:[],2:[],3:[], 4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[],16:[],17:[],18:[],19:[],20:[],21:[],22:[],23:[],24:[],25:[],26:[],27:[],28:[],29:[],30:[],31:[],32:[]}
test_set = {1:[],2:[],3:[], 4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[],16:[],17:[],18:[],19:[],20:[],21:[],22:[],23:[],24:[],25:[],26:[],27:[],28:[],29:[],30:[],31:[],32:[]}
train_data = data[0]
test_data =data[1]
#print(train_data)
print("#"*100)
#print(test_data)

for i in train_data:
    #print(i[0])
    #print(i[0].__len__())
    #print(i[1][0])
    train_set[int(i[-1])].append(i[:-1])
#print("*"*50)
for i in test_data:
    #print(i[1][0])
    test_set[int(i[-1])].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbors(train_set, data, k=3)
        if group == vote:
            correct += 1
        total += 1
print('Accuracy:', correct/total)