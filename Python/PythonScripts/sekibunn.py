#Pythonで積分の計算
#http://org-technology.com/posts/integrate-function.html
from sympy import *

# symbolの宣言をしてから使う
x, y = symbols("x y")

#関数の定義
f=x**2
l=exp(y)
#積分
integrate(f, x)
integrate(f, (x,0,1))
integrate(exp(-x), (x, 0, oo))
