from math import exp,sqrt,log
from scipy.stats import norm

#通常のBS公式
def BS_Call(S0, sigma ,r,q,T,K):
    d1 = (log(S0 / K) + (r-q + sigma**2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    BS_Call = S0 *exp(-q*T)* norm.cdf(x=d1, loc=0, scale=1) - K * exp(-r * T) * norm.cdf(x=d2, loc=0, scale=1)
    return BS_Call
def BS_Put(S0, sigma ,r,T,K):
    d1 = (log(S0 / K) + (r + sigma**2 / 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    BS_Put = K * exp(-r * T) * norm.cdf(x=-d2, loc=0, scale=1)-S0 *exp(-q*T)* norm.cdf(x=-d1, loc=0, scale=1) 
    return BS_Put
#バリアオプションの公式

#alpha
alpha=2*(r-q)/sigma**2-1
def d1(g):
    d1_g=(log(g)+(r-q)*T)/(sigma*sqrt(T))+sigma*sqrt(T)/2
    return d1_g
def d2(g):
    d2_g=(log(g)+(r-q)*T)/(sigma*sqrt(T))-sigma*sqrt(T)/2
    return d2_g
def Chat(h,f,g,A):
    Chat=h*(f*exp(-q*T)*norm.cdf(d1(g))+A*exp(-r*T)*norm.cdf(d2(g)))
    return Chat
def Phat(h,f,g,A):
    Phat=h*(-f*exp(-q*T)*norm.cdf(-d1(g))-A*exp(-r*T)*norm.cdf(-d2(g)))
    return Phat
def SBCall(a0,a1,a2,a3):#シングルバリアコール
    C0=Chat(1,S,S/K,-K)
    C1=Chat(1,S,S/B,-K)
    C2=Chat((B/S)**alpha,(B**2)/S,(B**2)/(K*S),-K)
    C3=Chat((B/S)**alpha,(B**2)/S,B/S,-K)
    SBCall=a0*C0+a1*C1+a2*C2+a3*C3
    return SBCall
def SBPut(a0,a1,a2,a3):#シングルバリアプット
    P0=Phat(1,S,S/K,-K)
    P1=Phat(1,S,S/B,-K)
    P2=Phat((B/S)**alpha,(B**2)/S,(B**2)/(K*S),-K)
    P3=Phat((B/S)**alpha,(B**2)/S,B/S,-K)
    SBPut=a0*P0+a1*P1+a2*P2+a3*P3
    return SBPut
def DBCall(a0,a1,a2,a3,a4,a5,a6):#ダブルバリアコール
    C0=Chat(1,S,S/K,-K)
    def C1(n):
        return Chat((U/L)**(n*alpha),((U/L)**(2*n))*S,(S/K)*(U/L)**(2*n),-K)
    def C2(n):
        return Chat((U/L)**(n*alpha),((U/L)**(2*n))*S,(S/U)*(U/L)**(2*n),-K)
    def C3(n):
        return Chat((U/L)**(n*alpha),((U/L)**(2*n))*S,(S/L)*(U/L)**(2*n),-K)
    def C4(n):
        return Chat(((L/S)**alpha)*((L/U)**(n*alpha)),((L**2)/S)*((L/U)**(2*n)),((L**2)/(K*S))*((L/U)**(2*n)),-K)
    def C5(n):
        return Chat(((L/S)**alpha)*((L/U)**(n*alpha)),((L**2)/S)*((L/U)**(2*n)),((L**2)/(U*S))*((L/U)**(2*n)),-K)
    def C6(n):
        return Chat(((L/S)**alpha)*((L/U)**(n*alpha)),((L**2)/S)*((L/U)**(2*n)),(L/S)*((L/U)**(2*n)),-K)
    def C(n):
        return a1*C1(n)+a2*C2(n)+a3*C3(n)+a4*C4(n)+a5*C5(n)+a6*C6(n)
    Csum=sum(C(n) for n in range(-10,11))
    return a0*C0+Csum
def DBPut(a0,a1,a2,a3,a4,a5,a6):#ダブルバリアプット
    P0=Phat(1,S,S/K,-K)
    def P1(n):
        return Phat((U/L)**(n*alpha),((U/L)**(2*n))*S,(S/K)*(U/L)**(2*n),-K)
    def P2(n):
        return Phat((U/L)**(n*alpha),((U/L)**(2*n))*S,(S/U)*(U/L)**(2*n),-K)
    def P3(n):
        return Phat((U/L)**(n*alpha),((U/L)**(2*n))*S,(S/L)*(U/L)**(2*n),-K)
    def P4(n):
        return Phat(((L/S)**alpha)*((L/U)**(n*alpha)),((L**2)/S)*((L/U)**(2*n)),((L**2)/(K*S))*((L/U)**(2*n)),-K)
    def P5(n):
        return Phat(((L/S)**alpha)*((L/U)**(n*alpha)),((L**2)/S)*((L/U)**(2*n)),((L**2)/(U*S))*((L/U)**(2*n)),-K)
    def P6(n):
        return Phat(((L/S)**alpha)*((L/U)**(n*alpha)),((L**2)/S)*((L/U)**(2*n)),(L/S)*((L/U)**(2*n)),-K)
    def P(n):
        return a1*P1(n)+a2*P2(n)+a3*P3(n)+a4*P4(n)+a5*P5(n)+a6*P6(n)
    Psum=sum(P(n) for n in range(-10,11))
    return a0*P0+Psum

UOCBK0,0,0,0
UOCKB0,-1,-1,1
UICBK1,0,0,0
UICKB0,1,1,-1
DOCBK1,0,-1,0
DOCKB0,1,-1,-1
DICBK0,0,1,0
DICKB1,-1,0,1
UOPBK0,1,0,-1
UOPKB1,0,-1,0
UIPBK1,-1,0,1
UIPKB0,0,1,0
DOPBK1,-1,-1,1
DOPKB0,0,0,0
DIPBK0,1,1,-1
DIPKB1,0,0,0


S=100.0
sigma=30/100
r=5/100
q=0.0
T=1
K=100.0
B=80.0
U=120.0
L=80.0
SBCall(1,0,-1,0)
DBCall(0,1,-1,0,-1,1,0)
