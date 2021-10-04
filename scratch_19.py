import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import  train_test_split
from sklearn import  linear_model
from sklearn import metrics
from sklearn.metrics import accuracy_score
import numpy as np
xx=np.array([1,2,3,4,5,6,7])

yy=np.array([0,5,3,9,6,7,4])
boston=datasets.load_boston()
x=boston.data
y=boston.target
x_tr,x_te,y_tr,y_te = train_test_split(x,y,test_size=0.2)
lreg=linear_model.LinearRegression()
#print(boston.describe())

model=lreg.fit(x_tr,y_tr)
prediction= model.predict(x_te)
#plt.scatter(x_te,prediction)
#plt.plot(x_te,prediction)
#print(prediction)
print("the results are here")

#print(prediction )
print("babliram")
#print(y_te)
print("bachuram")
for i in lreg.coef_:
  print(i," coeff")
print(model)
#print("accuracy_score",accuracy_score(y_te,prediction))
accuracy=accuracy_score(y,y_te)
print("accuracy is :",accuracy)
print("mean square error",metrics.mean_squared_error(y_te,prediction))
predict =model.predict(5)
print()
plt.show()
