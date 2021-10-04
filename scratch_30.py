import pandas as pd
import quandl
import  math
import numpy as np
from sklearn import preprocessing  ,svm
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import  pickle
style.use('ggplot')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression

df=quandl.get('WIKI/GOOGL')

df =df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['Hl_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.0
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.0
df=df[['Adj. Close','Hl_PCT','PCT_change','Adj. Volume']]
forecast_col ='Adj. Close'
print(len(df))
df.fillna(-9999,inplace=True)
forecast_out =int(math.ceil(0.01*len(df)))
df['label']=df[forecast_col].shift(-forecast_out)
a=np.array([9,2,3,4,7,6,7,8,9])
a=a[2:]



x=np.array(df.drop(['label'],1))

x=preprocessing.scale(x)
x=x[:-forecast_out]
x_lately=x[-forecast_out:]
df.dropna(inplace=True)
y=np.array(df['label'])
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2)

model=  LinearRegression(n_jobs=1)
model.fit(x_train,y_train)
accuracy = model.score(x_test,y_test)

forecast_set =model.predict(x_lately)

df['Forecast']=np.nan
print(df['Forecast'])
last_date=df.iloc[-1].name
last_unix=last_date.timestamp()
one_day =86400
next_unix =last_unix +one_day
print(last_date)
print('bachuram')
print(last_unix)
for i in forecast_set:
    next_date =datetime.datetime.fromtimestamp(next_unix)
    next_unix +=one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('date')
plt.ylabel('price')
plt.show()