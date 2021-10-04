from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
xx=np.array([1,2,3,4,5,6,7])
yy=np.array([5,3,4,2,8,9,7])



model =LinearRegression()
xx=xx.reshape(-1,1)
yy =yy.reshape(-1,1)
model.fit(xx,yy)
yt = model.predict(xx)

plt.scatter(xx,yy)
plt.plot(xx,yt)
plt.show()



