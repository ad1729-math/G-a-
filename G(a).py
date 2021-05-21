#The code for G(a). Author:Alapan Das

import math as m


def primality(p):
    count=1
    for i in range(2,p):
        if p%i!=0:
            count=count*1
        else:
            count=count*0
            break
    return count
 
def factor(n):    
    l=[]
    a=[]
    for P in range(3,int(n/2)+1):
        if primality(P)==1:
            if  n%P==0:
                l.append(P)
                for r in range(1, 5):
                    s=m.pow(P,r)
                    if n%s!=0:
                       a.append(r-1)
                       break
                    else:
                        continue
            else:
                continue
        else:
            continue
    T=list(zip(l,a))
    return T

S=[]

def G(a):
    for k in range(1, 50):
        s=m.pow(2, k)
        if  a%s!=0:
            r0=k-1
            break
        else:
            continue

    if  r0==0:
        z=0
    else:
        g=1
        T=factor(a)
        r=len(T)
        for i in range(0, r):
            g=g*(T[i][1]+1-(T[i][1])/(T[i][0]))
        z=a*(r0/2*g-1)
    return z


a=int(input('enter the number'))
K=round(G(a))
print(K)








    











