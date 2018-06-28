from math import exp,sqrt
import random
import time
def gBM(S,sigma,mu,t,z):
    gBM= S*exp((mu - sigma**2/2)*t + sigma * sqrt(t) * z)
    return gBM


def MCDownAndOut_Call(S0,sigma,r,T,K,B,Tsteps,SampleNo):
    start_time = time.time()#処理時間計測開始
    SumPayoff = 0.0
    消滅数 = 0.0
    計算誤差バッファ = Tsteps / 100
    for i in range(SampleNo):
        現時点 = 0 #ゼロからスタートして株価<=Lをチェック
        S = S0
        満期以前 = True
        生存 = True
        while 生存 and 満期以前:
            if S <= B:
                生存 = False
            else:
                現時点 = 現時点 + Tsteps #満期前なら次のステップをチェック
                if 現時点 <= T + 計算誤差バッファ:
                    z=random.gauss(0,1)
                    S = gBM(S, sigma, r, Tsteps, z)
                else:
                    満期以前 = False
        if 生存 == False  :
            消滅数 = 消滅数 + 1
        else:
            Payoff = max(S - K, 0)
            SumPayoff = SumPayoff + Payoff
    OptionPrice = SumPayoff / SampleNo * exp(-r * T)
    extinction=消滅数 / SampleNo
    duration = time.time() - start_time#処理時間計測終了
    return "Price=",OptionPrice, "Calc. time=",duration,"消滅割合=" ,extinction

S0=100.0
sigma=30/100
r=5/100
T=0.5
K=100.0
B=80.0
Tsteps=0.01
SampleNo=10000
MCDownAndOut_Call(S0,sigma,r,T,K,B,Tsteps,SampleNo)
