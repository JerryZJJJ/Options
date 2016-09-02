import numpy as np
import math as m

def AmericanOp (n, S, K, r, v, T, PC):

    dt = T/n                    #time step
    u = m.exp(v*m.sqrt(dt))     #u up motion
    d = 1/u                     #d down motion
    p = (m.exp(r*dt)-d)/(u-d)   #probabilities of up or down for call

    Sm = np.zeros((n+1, n+1))   #declare stock price tree
    Cm = np.zeros((n+1, n+1))   #declare option price tree

    for j in range(n+1):
        for i in range(j+1):
            Sm[i,j] = S*m.pow(d,i) * m.pow(u,j-i)        #fill in stock price tree

    for j in range(n+1, 0, -1):
        for i in range(j):
            if (PC == 1):                               #1 for put
                if(j == n+1):
                    Cm[i,j-1] = max(K-Sm[i,j-1], 0)     #fill in final nodes of options tree
                else:
                    Cm[i,j-1] = m.exp(-.05*dt) * (p*Cm[i,j] + (1-p)*Cm[i+1,j])  #fill all other nodes
            if (PC == 0):                               #0 for call
                if (j == n + 1):
                    Cm[i,j-1] = max(Sm[i,j-1]-K, 0)     #fill n final nodes of options tree
                else:
                    Cm[i,j-1] = m.exp(-.05*dt) * (p*Cm[i,j] + (1-p)*Cm[i+1,j])  #fill all other nodes

    #print (Cm)
    return Cm[0,0] #price option at time 0

if __name__ == "__AmericanOp__":
    S = 100
    k = 100
    r = .05
    v = .3
    T = 200/365
    n = 3
    PC = 0
    x = AmericanOp(n,S,k,r,v,T,PC)
    PC = 1
    y = AmericanOp(n, S, k, r, v, T, PC)
    print(x)
    print(y)






