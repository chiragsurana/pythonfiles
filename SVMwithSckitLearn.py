import pandas as pd
import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
x=iris.data[:,:2]
y=iris.target

x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
X_plot = np.c_[xx.ravel(), yy.ravel()]
C = 1.0
# Svc_classifier = svm.SVC(kernel='linear', C=C).fit(x, y)
# Z = Svc_classifier.predict(X_plot)
# Z = Z.reshape(xx.shape)
plt.figure(figsize=(15, 5))

# plt.contourf(xx, yy, Z, cmap=plt.cm.tab10, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Set1)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('Support Vector Classifier with linear kernel')
print('bachuram')