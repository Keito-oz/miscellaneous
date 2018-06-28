#多次元正規分布の累積分布関数

#多次元正規分布の密度関数を定義
#import numpy as np
import sympy
#平均と分散
m=Matrix([0,0])
s=Matrix([[1,0],[0,1]])
#rho=Symbol("rho")最後でうまくいかない
s_rho=Matrix([[1,0.3],[0.3,1]])
d=s_rho.det()        #行列式
s_inv=s_rho.inv()   #逆行列

#ガウス二次元確率密度を返す関数
x1, x2 = symbols("x1 x2")
x=Matrix([x1,x2])
pdf=exp((-(x-m).T*s_inv*(x-m)/2))/(2*pi*sqrt(d))

#分布関数の計算
z1,z2=symbols("z1 z2")
integrate(integrate(pdf,(x1,-oo,oo)),(x2,-oo,oo)).evalf()  #1になる、ok
cdf=integrate(integrate(pdf,(x1,-oo,z1)),(x2,-oo,z2))       #Integralを含んだ式になる
#このIntegralを個別に計算してもできない
cdf.subs([(z1,oo),(z2,oo)]).evalf(10)                                   #これもIntを含んだ式になる。



#以下メモ
cdf.subs([(z1,1),(z2,1)]).evalf()

I1=integrate(pdf.evalf(),(x1,-oo,1))
I2=integrate(I1,(x2,-1,1)).evalf()
I2.evalf()

cdf=integrate(integrate(pdf,(x1,-oo,oo)),(x2,-oo,oo)).evalf()
#10桁精度で
cdf=integrate(integrate(pdf,(x1,-oo,z1)).evalf(10),(x2,-oo,z2)).evalf(10)

nakami1=exp(-0.549450549450549*x1**2)*exp(0.32967032967033*x1*x2)
nakami2=Integral(nakami1, (x1, -oo, oo)).evalf(10)
0.1668397135*Integral(exp(-0.549450549450549*x2**2)*nakami2, (x2, -oo, oo))

pdf_v=pdf.evalf(5)
f1=integrate(pdf_v,(x1,-oo,0.1)).evalf(5)
cdf000=integrate(f1,(x2,-oo,z2)).evalf(5)

#Reference
二次元正規分布のコーディング例はこちらを参考にした
https://openbook4.me/projects/231/sections/1538
Sympyで関数に値を代入する方法
http://programming.blogo.jp/python/sympy/%E9%96%A2%E6%95%B0%E3%81%AB%E4%BB%A3%E5%85%A5
Sypmyで積分計算をする方法と数値評価evalfについて
http://www.turbare.net/transl/scipy-lecture-notes/packages/sympy.html
行列の転置についてはこちら
http://mathharachan.hatenablog.com/entry/2016/03/07/213938
当初np.expを使った際にエラーを履いた時の処理はこちら
http://stackoverflow.com/questions/29840669/attributeerror-add-object-has-no-attribute-log-python
行列式と逆行列の計算
https://showa-yojyo.github.io/notebook/python-sympy/matrices.html
行列の掛け算はこちらを参考
http://takuyaokada.hatenablog.com/entry/20160219/1455854929
正規分布いっぱん
https://ja.wikipedia.org/wiki/%E6%AD%A3%E8%A6%8F%E5%88%86%E5%B8%83#.E5.A4.9A.E5.A4.89.E9.87.8F.E6.AD.A3.E8.A6.8F.E5.88.86.E5.B8.83
数式における等式
http://www.irohabook.com/latex-eqnarray
