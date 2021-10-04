import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('iris.csv')
names=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
from sklearn.preprocessing import StandardScaler

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
# Separating out the features
x = data.loc[:, names].values
# Separating out the target
#y = data.loc[:,['target']].values
# Standardizing the features
y = StandardScaler().fit_transform(x)
from sklearn.decomposition import PCA
pca = PCA(0.95)
principalComponents = pca.fit_transform(y)
principalDf = pd.DataFrame(data = principalComponents)
print(data.head())
finaldf = pd.concat([principalDf, data[['Species']]], axis = 1)
print(finaldf.head())
print(data.loc[:,'Id'])
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finaldf['Species'] == target
    ax.scatter(finaldf.loc[indicesToKeep, 'principal component 1']
               , finaldf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

