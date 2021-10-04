# importing scikit learn with make_blobs
from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import load_iris
import  pandas as pd
pd.
iris = load_iris()
print(iris)

import numpy as np
# creating datasets X containing n_samples
# Y containing two classes
X, Y = make_blobs(n_samples=50, centers=2,random_state=0, cluster_std=.5)
import matplotlib.pyplot as plt

# plotting scatters
print(X,Y)

plt.scatter(X[:, 0], X[:, 1], c=Y, s=40, cmap='spring')
plt.legend("showhjhkhk")
# creating line space between -1 to 3.5
xfit = np.linspace(-1, 3.5)

# plotting scatter
#plt.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='spring')

# plot a line between the different sets of data

    

plt.xlim(-1, 3.5)

plt.show()
plt.show()