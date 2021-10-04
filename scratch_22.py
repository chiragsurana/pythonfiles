import numpy as np
import pandas as pd


data=pd.read_csv('b.csv')
print(data.head())
print(data.iloc["Country":"Canada"])