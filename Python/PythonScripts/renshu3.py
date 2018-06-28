import os
os.chdir('C:\\Users\\ozaw0540\\Documents\\PythonScripts')
import numpy as np
reactions_in_ms=np.loadtxt('reactions.txt')
print(reactions_in_ms.size)
print(reactions_in_ms[:20])
reactions_in_sec=reactions_in_ms/1000
print(reactions_in_sec[:20])
print("平均：",np.mean(reactions_in_sec))
print("標準偏差：",np.std(reactions_in_sec))

import matplotlib.pyplot as plt
h=plt.hist(reactions_in_sec)
plt.show(h)

a=np.array([0,1,2,3])
A=np.array([[1,0,0],[0,1,0],[0,0,1]])
zeros=np.zeros(10)
zeroMatrix=np.zeros(9).reshape(3,3)

a=np.arange(1,10).reshape(3,3)
np.sum(a,axis=0)
a[0,0]

s=np.sin(np.pi*np.arange(0.0,2.0,0.01))
t=plt.plot(s)
plt.show(t)

x=np.random.randn(5000)
y=np.random.randn(5000)
t=plt.plot(x,y,'o',alpha=0.1)
plt.show(t)

x=np.array([1.628,3.363,5.145,7.683,9.855])
y=np.array([1.257,3.672,5.841,7.951,9.775])

a=np.array([x,np.ones(x.size)])
a=a.T
m,c=np.linalg.lstsq(a,y)[0]
t=plt.plot(x,y,'o')
s=plt.plot(x,(m*x+c))
plt.show(t)
plt.show(s)


