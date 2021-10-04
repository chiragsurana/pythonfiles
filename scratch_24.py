import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('b.csv')
sns.scatterplot(df.loc['Country'],df.loc['Month Name'])
print(df.head())