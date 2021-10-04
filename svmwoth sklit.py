import numpy as np
from sklearn.preprocessing import  MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
url = 'http://bit.ly/2cLzoxH'
dataset=pd.read_csv(url)
print(dataset.country.value_counts())

isCountry= (dataset.continent.isin(['Asia'])) & (dataset.year== 2007)
x=dataset[isCountry]
x=x.sort_values("lifeExp", axis = 0, ascending = True )
x.rename({"country":"Countryff"},axis= "columns")
print(x)
print(sum(x.gdpPercap))
plt.barh(x.country,x.lifeExp)
plt.axvline(50,color='black')
plt.axvline(60,color='black')
plt.axvline(70,color='black')
# xx=x['year']
# yy=x['lifeExp']
# plt.scatter(xx,yy)
# plt.plot(xx,yy)
# print(dataset.head(10))
plt.show()
