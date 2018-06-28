import numpy as np
import matplotlib.pyplot as plt
from math import exp,sqrt
import random
sigma=0.3
mu=0.05
delta_t=0.01
process=np.zeros(10000)#10,000ステップ
process[0]=100#初期値
def gBM(S,sigma,mu,t,z):#幾何ブラウン運動を関数にしておく
    gBM= S*exp((mu - sigma**2/2)*t + sigma * sqrt(t) * z)
    return gBM
for n in range(1,len(process)):
    process[n]=gBM(process[n-1],sigma,mu,delta_t,random.gauss(0,1))

plt.plot(process)
plt.show()

def plt_process(Step,Sample):
    process_matrix=np.zeros((Step,Sample))
    process_matrix[0,:]=100#初期値
    def gBM(S,sigma,mu,t,z):#幾何ブラウン運動を関数にしておく
        gBM= S*exp((mu - sigma**2/2)*t + sigma * sqrt(t) * z)
        return gBM
    for i in range(1,Step):
        for n in range(Sample):
            process_matrix[i,n]=gBM(process_matrix[i-1,n],sigma,mu,1/Step,random.gauss(0,1))
    plt.plot(process_matrix)
    plt.show()
plt_process(1000,20)
