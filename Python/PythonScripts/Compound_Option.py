#インプット
S0=100
sigma=30/100
r=5/100
q=0/100
T1=1
T2=2
K1=20
K2=100
SampleT1=100
SampleT2=100
SampleOP=100

#コンパウンド・オプションの解析解による評価
from scipy.stats import norm, mvn
from scipy import exp,log,sqrt,optimize,pi,sign
import numpy as np

def BS_Call(S, sigma ,r,q,T,K):
    d1 = (log(S / K) + (r -q+ sigma**2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    BS_Call = S * exp(-q * T) * norm.cdf(x=d1, loc=0, scale=1) \
             -K * exp(-r * T) * norm.cdf(x=d2, loc=0, scale=1)
    return BS_Call

BS_Call(S0, sigma ,r,q,T1,K2)
14.231254785985819

def h(S_sol):
    return BS_Call(S_sol, sigma ,r,q,T2-T1,K2)-K1

del a,b,c,A,B

def M(a,b,c):
    def M_base(a,b,c):
        A=np.array([0.3253030,0.4211071,0.1334425,0.006374323])
        B=np.array([0.1337764,0.6243247,1.3425378,2.2626645])
        def f_M(B_1,B_2):
            a_prime=a/sqrt(2*(1-c**2))
            b_prime=b/sqrt(2*(1-c**2))
            return exp(a_prime*(2*B_1-a_prime)+b_prime*(2*B_2-b_prime)+2*c*(B_1-a_prime)*(B_2-b_prime))
        SUM=0
        for n in range(4):
            for m in range(4):
                SUM=SUM+A[n]*A[m]*f_M(B[n],B[m])
        return sqrt(1-c**2)/pi*SUM
    if a<0 and b<0 and c<0:
        return M_base(a,b,c) 
    elif a<0 and b>0 and c>0:
        return norm.cdf(x=a, loc=0, scale=1)-M_base(a,-b,-c)
    elif a>0 and b<0 and c>0:
        return norm.cdf(x=b, loc=0, scale=1)-M_base(-a,b,-c)
    elif a>0 and b>0 and c<0:
        return norm.cdf(x=a, loc=0, scale=1)+norm.cdf(x=b, loc=0, scale=1)-1+M_base(-a,-b,c)
    else:
        c1=(a*c-b)*sign(a)/sqrt(a**2-2*c*a*b+b**2)
        c2=(b*c-a)*sign(b)/sqrt(a**2-2*c*a*b+b**2)
        delta=(1-sign(a)*sign(b))/4
        return M_base(a,0,c1)+M_base(b,0,c2)-delta

#test
M(0.2,0.2,sqrt(T1/T2))
0.45686894933768613
def M_MVN(a,b,c):
    from scipy.stats import mvn
    mean = np.array([0,0])
    Sigma = np.array([[1,c],[c,1]])
    lower=np.array([-10000,-10000])
    upper=np.array([a,b])
    p,i=mvn.mvnun(lower,upper,mean,Sigma)    
    return p
M_MVN(0.2,0.2,sqrt(T1/T2))
0.45686899301606676

#これでばっちり！
def CoC_AN(S0,T1,T2,K1,K2):
    S_star=float(optimize.fsolve(h,100))
    a1 = (log(S0 / S_star) + (r-q + sigma**2 / 2) * T1) / (sigma * sqrt(T1))
    a2 = a1 - sigma * sqrt(T1)
    b1 = (log(S0 / K2) + (r-q + sigma**2 / 2) * T2) / (sigma * sqrt(T2))
    b2 = b1 - sigma * sqrt(T2)
    CoC_AN = S0  * exp(-q * T2)*M(a1,b1,sqrt(T1/T2))\
          - K2 * exp(-r * T2) *M(a2,b2,sqrt(T1/T2))\
          -K1* exp(-r * T1) *norm.cdf(x=a2, loc=0, scale=1)
    return CoC_AN

def CoC_AN_MVN(S0,T1,T2,K1,K2):
    S_star=float(optimize.fsolve(h,100))
    a1 = (log(S0 / S_star) + (r-q + sigma**2 / 2) * T1) / (sigma * sqrt(T1))
    a2 = a1 - sigma * sqrt(T1)
    b1 = (log(S0 / K2) + (r-q + sigma**2 / 2) * T2) / (sigma * sqrt(T2))
    b2 = b1 - sigma * sqrt(T2)
    CoC_AN = S0  * exp(-q * T2)*M_MVN(a1,b1,sqrt(T1/T2))\
          - K2 * exp(-r * T2) *M_MVN(a2,b2,sqrt(T1/T2))\
          -K1* exp(-r * T1) *norm.cdf(x=a2, loc=0, scale=1)
    return CoC_AN

CoC_AN(S0,T1,T2,K1,K2)
8.9321683093744433
CoC_AN_MVN(S0,T1,T2,K1,K2)
CoC_AN(S0, 0,1,0,100)

#検算
S_star_test=optimize.fsolve(h,14)
a1_test = float((log(S0 / S_star_test) + (r-q + sigma**2 / 2) * T1) / (sigma * sqrt(T1)))#arrayを数値に変換
a2_test = a1_test - sigma * sqrt(T1)
b1_test = (log(S0 / K2) + (r-q + sigma**2 / 2) * T2) / (sigma * sqrt(T2))
b2_test= b1_test - sigma * sqrt(T2)
M(a2_test,b2_test,sqrt(T1/T2))

from scipy.stats import mvn
import numpy as np
mu = np.array([0,0])
S = np.array([[1,rho],[rho,1]])
low_inf=np.array([-10000,-10000])
upp=np.array([a2_test,b2_test])
mvn.mvnun(low_inf,upp,mu,S)


#コンパウンド・オプションのモンテカルロ法による評価
import random
import numpy as np
from scipy import exp,log,sqrt


def gBM(S,sigma,mu,t,z):
    gBM= S*exp((mu- sigma**2/2)*t + sigma * sqrt(t) * z)
    return gBM

def BSMC_Call(S_t,K,T,n):
    S_T=np.zeros(n)             #権利行使日の株価を格納する配列
    Call_T=np.zeros(n)          #各株価に対応するオプション価格の配列
    Sum_Call_T=0                #Σmax(S_T-K,0)を計算するための変数
    for j in range(n):      
        S_T[j]=gBM(S_t,sigma,r-q,T,random.gauss(0,1))
        Call_T[j]= max(S_T[j]- K, 0)
        Sum_Call_T=Sum_Call_T+Call_T[j]
    Expected_Call_Value=Sum_Call_T / n
    Call_Value=exp(-r*T)*Expected_Call_Value #現在価値に割り引く
    return Call_Value

def CoC_MC(S0,K1,K2,T1,T2,SampleT1,SampleOP,SampleT2):
    S_T1=np.zeros(SampleT1)
    S_T2=np.zeros(SampleT1*SampleT2)
    Call_T1=np.zeros(SampleT1)
    Call_T2=np.zeros(SampleT1*SampleT2)
    Sum_Call=0
    for n in range(SampleT1):      
        S_T1[n]=gBM(S0,sigma,r-q,T1,random.gauss(0,1))
        Call_T1[n]=BSMC_Call(S_T1[n],K2,T2-T1,SampleOP)
        if Call_T1[n]>K1:
            for m in range(SampleT2):
                S_T2[n*SampleT1+m]=gBM(S_T1[n],sigma,r-q,T2-T1,random.gauss(0,1))
                Call_T2[n*SampleT1+m]=max(S_T2[n*SampleT1+m]-K2,0)
                Sum_Call=Sum_Call+Call_T2[n*SampleT1+m]-exp(r*(T2-T1))*K1
    Expected_CoC_Value=Sum_Call / SampleT1/SampleT2
    CoC_Value=exp(-r*T2)*Expected_CoC_Value 
    return CoC_Value


CoC_AN(100, sigma ,r,q,1,2,100,100)
CoC_MC(100,20,100,1,2,100,100,100)

#Memo
from scipy.stats import multivariate_normal
import numpy as np
low = np.array([-10, -10])
upp = np.array([.1, -.2])
mu = np.array([-.3, .17])
S = np.array([[1.2,.35],[.35,2.1]])
p,i = mvn.mvnun(low,upp,mu,S)
print p


    A1 = 0.3253030
    A2 = 0.4211071
    A3 = 0.1334425
    A4 = 0.006374323
    B1 = 0.1337764
    B2 = 0.6243247
    B3 = 1.3425378
    B4 = 2.2626645
