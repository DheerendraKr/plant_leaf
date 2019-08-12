import pickle
import numpy as np
from sklearn.svm import SVC


#file=open("svm_plant_feature_set.pickle","rb")
file=open("svm_plant_feature_set.pickle","rb")
data=pickle.load(file)
 

test_data=data[1]
x_test=[]
y_test=[]

for i in test_data:
    x_test.append(i[:-1])
    y_test.append(i[-1])

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
result = loaded_model.score(x_test, y_test)
print(result)

feature=np.array([x_test[11]])
print(feature)
feature.reshape(1,-1)
print(feature)
res=loaded_model.predict(feature)
print(res)
print(res.__len__())