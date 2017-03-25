import numpy as np
import matplotlib.pyplot as plt


def L(q):
    return np.exp(-q**2)

def LogL(q):
    return -q**2

def difLogL(q):
    return -2*q

def p_0():
    return np.random.normal()

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

n=100
q=np.zeros(n)
p=np.zeros(n)
q[0]=np.random()
p[0]=p_0

