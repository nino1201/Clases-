import numpy as np
import matplotlib.pyplot as plt

cosas=np.genfromtxt('fake_regression.txt')

trainx=cosas[:int(len(cosas)*0.75),0]
testx=cosas[int(len(cosas)*0.75):,0]

trainy=cosas[:int(len(cosas)*0.75),1]
testy=cosas[int(len(cosas)*0.75):,1]
n=21


ECPtr=np.zeros(n)
ECPtest=np.zeros(n)

def coef(x,y,i):
    return np.polyfit(x,y,i)

def pol(x,p):
    pol=0
    for j in range(len(p)):
        pol+=p[j]*x**(j)

    return pol

def ECP(y,f):
    return sum((y-f)**2)/len(y)

for i in range(n):
    co=coef(trainx,trainy,i)
    
    ECPtr[i]=ECP(trainy,pol(trainx,co))
    ECPtest[i]=ECP(testy,pol(testx,co))
         
print np.argmin(abs(ECPtr-ECPtest)**2)

