#SciPy.Optimazeを使う方法
from scipy import optimize, exp
def f(x):
    return x**2-5*x+2
def g(x):
    return exp(x)
def h(x):
    return f(x)-g(x)

optimize.fsolve(h,0) #0近辺から解を探索

#ニュートン法
from math import exp
def f(x):
    return x**2-5*x+2
def g(x):
    return exp(x)
def h(x):
    return f(x)-g(x)
def h_prime(x):
    return 2*x-5-exp(x)

def Newton(ini,err):
    x_n=ini
    x_n_scc=0
    count=0
    while True:
        count=count+1
        x_n_scc=x_n-h(x_n)/h_prime(x_n)
        if h(x_n_scc)<err:
            break
        x_n=x_n_scc
    print(\
        "数値解は",x_n_scc,\
        "\nその時の関数の値は",h(x_n_scc),\
        "\n計算回数は",count,"です")

Newton(0,1/100000)#0近辺から解を探索、誤差1/100000未満

#バイナリーサーチ法
from math import exp
def f(x):
    return x**2-5*x+2
def g(x):
    return exp(x)
def h(x):
    return f(x)-g(x)

def BinarySearch(upper,lower,err):
    up=upper
    low=lower
    count=0
    while True:
        count=count+1
        mid=(up+low)/2
        y=h(mid)
        if abs(y)<1/100000:#解が発見された
            break
        elif h(low)*y<0:#解は下限と中間点の間にある
            up=mid
        else:                     #解は上限と中間点の間にある
            low=mid
    print(\
        "数値解は",mid,\
        "\nその時の関数の値は",y,\
        "\n計算回数は",count,"です")
    
BinarySearch(1,-1,1/10000000)
#SymPyを使う方法＝数値的には解けない
from sympy import *
x=Symbol("x")
f=x**2-5*x+2
g=exp(x)

h=f-g
h.subs([(x,0.1689)])
#ほぼ0

solve(h,x)
#無理
