from scipy import optimize, exp,log,sqrt
from scipy.stats import norm

def BS_Call(S0, sigma ,r,q,T,K):
    d1 = (log(S0 / K) + (r-q + sigma**2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    BS_Call = S0  * exp(-q * T)* norm.cdf(x=d1, loc=0, scale=1) \
    - K * exp(-r * T) * norm.cdf(x=d2, loc=0, scale=1)
    return BS_Call

S0=100
r=0.05
q=0.0
T=1
K=100
C_M=20

def h(sigma):
    h=BS_Call(S0, sigma ,r,q,T,K)-C_M
    return h

IV=optimize.fsolve(h,0)
>>> IV
array([ 0.45234036])


>>> BS_Call(S0, IV ,r,q,T,K)
array([ 20.])
