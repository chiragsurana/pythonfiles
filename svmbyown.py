import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

class Support_Vector_Machine :
    def _init_(self,visualization=True):
        self.visualization=visualization
        self.colors={1:'r',-1:"b"}
        if self.visualization:
            self.fig =plt.figure()
            self.ax=self.fig.add_subplot(1,1,1)

    def fit(self,data):
        self.data=data
        opt_dict ={ }
        transforms =[[1,1],
                     [-1,1],
                     [-1,-1],
                     [1,-1],]
        all_data =[]
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)
        self.mat_feature_value=max(all_data)
        self.min_feature_value =min(all_data)
        all_data =None
        step_sizes =[self.max_feature_value *0.1,
                     self.max_feature_value*0.01,
                     self.max_feature_value* 0.001,]
        b_range_multiple =5
        b_multiple =5
        latest_optimum =self.mat_feature_value*10
        for step in step_sizes:
            w=np.array([latest_optimum,latest_optimum])
            optimized = False
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_range_multiple),
                                   self.max_feature_value*b_range_multiple,
                                   step*b_multiple):
                    for transforma


    def predict(self,features):
        classification = np.sign(np.dot(np.array(features),self.w) +self.b)
        return classification

    data_dict = {-1:np.array([1,7],
                             [2,8],
                             [3,8],),
                 1:np.array([5,1],
                             [6,-1],
                             [7,3],)}