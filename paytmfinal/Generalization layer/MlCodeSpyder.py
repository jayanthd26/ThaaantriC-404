import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("DataSet.csv")    
X=dataset.iloc[:,4:-1].values
#x2=dataset.iloc[:,4:-1].values
x1=dataset.iloc[0:1,4:-1].values
#x3=dataset.iloc[0:3,4:-1].values

Y=dataset.iloc[:,-1].values        
#y2=dataset.iloc[:,-1].values
#Categorical Data:
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.externals import joblib
labelencoderX = LabelEncoder()     
  
X[:,1]=labelencoderX.fit_transform(X[:,1])
joblib.dump(labelencoderX,'LabelEncoderGender')

X[:,2]=labelencoderX.fit_transform(X[:,2])
joblib.dump(labelencoderX,'LabelEncoderPlace')

Y=labelencoderX.fit_transform(Y)
joblib.dump(labelencoderX,'LabelEncoderY')

"""
from sklearn.externals import joblib
joblib.dump(labelencoderX,'TrailModel1')
mj1=joblib.load('TrailModel1')
y2=mj.transform(y2)
x2[:,1]=mj1.transform(x2[:,1])

x1[:,1]=labelencoderX.transform(x1[:,1])
x1[:,2]=labelencoderX.transform(x1[:,2])
"""

hotencoder= OneHotEncoder(categorical_features=[-1])
X=hotencoder.fit_transform(X).toarray()
joblib.dump(hotencoder,"OneHotEncoderPlace")

#TrainingSet:
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

#ML Models:
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,Y_train)
joblib.dump(classifier,"MLModelLogisticRegression")

#Prediction

result=0
prob=prob[0].tolist()
dict1=dict(zip(prob,range(0,4)))
QueryCategory=np.array(['Fashion'])
if labelencoderX.transform(QueryCategory) in list(dict1.values())[1:4]:
    result=1
print(result)

#The score is 1.0(test) 0.00(train)

"""from sklearn.svm import SVC 
svm_model_linear = SVC(kernel = 'sigmoid', C = 1).fit(X_train, Y_train) 
svm_predictions = svm_model_linear.predict(X_test)    
accuracy = svm_model_linear.score(X_train, Y_train)
print(accuracy) The Score is 0.52(test) 0.4975(Train)"""

"""from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 3).fit(X_train, Y_train) 
accuracy = knn.score(X_train, Y_train) 
print(accuracy) The score is 1.0(test) 1.0(train) """

"""from sklearn.tree import DecisionTreeClassifier 
dtree_model = DecisionTreeClassifier(max_depth = 3).fit(X_train, Y_train) 
dtree_predictions = dtree_model.predict(X_test) 
accuracy = dtree_model.score(X_train,Y_train)
print(accuracy) The score on test is 1.0(test) and train is 1.0(train)"""