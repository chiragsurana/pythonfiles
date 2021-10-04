import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import datasets

data=pd.read_csv('iris.csv')

x= data.drop(['Species'],axis=1)
y=data.loc[:4].values
model=LinearRegression()


x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9)


model.fit(x_train,y_train)
predict=model.predict(x_test)
print(predict)
print(model)
print(data.describe())