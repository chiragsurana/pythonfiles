import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import accuracy_score
x=np.array([1,2,3,4,5,6])
y=np.array([3,7,8,9,11,12])
x=x.reshape(-1,1)
y=y.reshape(-1,1)
model=LinearRegression()
mod=LinearRegression()
model.fit(x,y)
poly=PolynomialFeatures(degree=5)
x_poly=poly.fit_transform(x)
mod.fit(x_poly,y)
y_poly=mod.predict(x_poly)

yt=model.predict(x)
plt.scatter(x,y,color='k',marker='.')

plt.plot(x,yt)
print(model.coef_,"the",model.intercept_)
test=np.array([1.5,2.5,3.5])
test=test.reshape(-1,1)
#acc=accuracy_score(y,yt)
print()
predict=model.predict(test)
print(predict)
plt.show()

