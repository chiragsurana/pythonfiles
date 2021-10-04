import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


x=np.array([1,2,3,4,5,6,7,8])
y=np.array([5,6,7,1,3,9,4,7])
x=x.reshape(-1,1)
y=y.reshape(-1,1)
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.3)
print(x_train,y_train)
model=LogisticRegression()
model.fit(x_train,y_train)
yy=model.predict(x_test)
print(yy,y_test)
