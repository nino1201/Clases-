import numpy as np
import matplotlib.pyplot as plt


def L(q):
    return np.exp(-q**2)

def LogL(q):
    return -q**2

def difLogL(q):
    return -2*q

def p_0():
    return np.random.normal(0,1)

def Leap_frog(p,q):
    N=
    qn=q
    pn=p
    for i in range(1,N):
        p_half=pn+0.5*e*difLogL(qn)
        qn=qn+e*p_half
        pn=p_half+0.5*e*difLogL(qn)
    return pn,qn

def H(p,q):
    K=0.5*p*p
    U=-LogL(q)
    return U+K

def HMC(steps):
    p=np.zeros(steps)
    q=np.zeros(steps)

    p[0]=p_0
    q[0]=p_0

    for i in range(1,steps):
        p[i]=p_0
        p_n,q_n=Leap_frog(p[i-1],q[i-1])

        E_n=H(pn,qn)
        E_o=H(p[i-1],q[i-1])
        
        a=min(1,np.exp(E_o-E_n))
        b=np.random.random()
        if b<a:
            q[i]=q_n
        else :
            q[i]=q[i-1]
    return q
n=100
q=np.zeros(n)
p=np.zeros(n)
q[0]=np.random()
p[0]=p_0

