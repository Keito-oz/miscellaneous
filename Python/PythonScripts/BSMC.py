import numpy as np
from math import exp,sqrt
import random
sigma=0.3
r=5/100
S_t=100
K=100
T=1

def gBM(S,sigma,mu,t,z):#幾何ブラウン運動を関数にしておく
    gBM= S*exp((mu- sigma**2/2)*t + sigma * sqrt(t) * z)
    return gBM


def BSMC_Call(n):
    S_T=np.zeros(n)             #権利行使日の株価を格納する配列
    Call_T=np.zeros(n)          #各株価に対応するオプション価格の配列
    Sum_Call_T=0                #Σmax(S_T-K,0)を計算するための変数
    for j in range(0,n-1):      
        S_T[j]=gBM(S_t,sigma,r,T,random.gauss(0,1))
        Call_T[j]= max(S_T[j]- K, 0)
        Sum_Call_T=Sum_Call_T+Call_T[j]
    Expected_Call_Value=Sum_Call_T / n
    Call_Value=exp(-r*T)*Expected_Call_Value #現在価値に割り引く
    return Call_Value

BSMC_Call(100000)
