import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import stats
x=np.array([1,2,3,4,5,300])
y=np.array([4,3,10,9,5])
t=preprocessing.StandardScaler()
t.fit(x)
print(t.transform(x))
print(preprocessing.normalize(x))
print(x)

x=x.reshape(-1,1)
mean=np.mean(x)
std=stats.stdev(x)
print(mean,"the",std)