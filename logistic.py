import numpy as np
import math
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
pre=[]
x=np.array([-1,0,-2,1,2,3,4,5])
y=np.array([5,3,6,2,5,4,11,13])
x=x.reshape(-1,1)
y=y.reshape(-1,1)
xt,xet,yt,yet=train_test_split(x,y,test_size=0.2)
pre=1/(1+np.exp(-x))
a=np.arange(-1000,1000,0.1)
print(a)
yy=1/(1+np.exp(a))
for i in pre:
    print(i)
    if i > 0.5 :
        print("1")
    else:
        print("0")


model=LogisticRegression()
model.fit(xt,yt)
predict=model.predict(xet)
plt.plot(0,1)
plt.plot(0,0,color="k")
plt.plot(a,math.sin(a))
plt.plot(a,yy)
plt.scatter(x,pre)
print(predict)
plt.show()
