import numpy as np
import matplotlib.pyplot as plt
import random as r

def probabilidad(l,x,a,b):
    ar=np.exp(-x[0]/l)/(-l*(np.exp(-b/l)-np.exp(-a/l)))
    
    for i in range(1,len(x)):
        ar*=np.exp(-x[i]/l)/(-l*(np.exp(-b/x[i])-np.exp(-a/l)))
    return ar 


def probLambda(l):
    return 1/100.

x=np.array([1.5,1.7,2.])
a=1.
b=20.
def problx(l,x,a,b):
    return probabilidad(l,x,a,b)*probLambda(l)

l=np.zeros(20000)
l[0]=r.random()
lr=np.linspace(0.01,7,20000)
for i in range(1,20000):
    l_new=l[i-1]+0.2*(r.random()-0.5)*2
    alpha=min(1,problx(l_new,x,a,b)/problx(l[i-1],x,a,b))

    u=r.random()
    if(u<alpha):
        l[i]=l_new
    else:
        l[i]=l[i-1]



plt.hist(l,bins=50,normed=True)
plt.plot(lr,problx(lr,x,a,b))
plt.show()
