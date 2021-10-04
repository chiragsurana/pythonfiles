from numpy import *

x=array([0,1,2,3,4,5])
y= array([4,6,7,9,4,6])
from scipy.interpolate import *
import  scipy.interpolate
p1=polyfit(x,y,1)
print(p1)
from matplotlib.pyplot import  *
xp=linspace(-2,6,100)

p2=polyfit(x,y,2)
p3=polyfit(x,y,3)
plot(xp,polyval(p1,xp),'r-')
plot(xp,polyval(p2,xp),'b--')
plot(xp,polyval(p3,xp),'m:')
plot(x,y,'o')
show()

