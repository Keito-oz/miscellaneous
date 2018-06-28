import matplotlib.pyplot as plt
Samples=100                 #描画するサンプルパスの数
Steps=10000      #時間区切りの数
S_T=np.zeros((Samples,Steps))  #
S_T[:,0]=S_t
for i in range(1,Samples):
    for j in range(1,Steps):     
        S_T[i,j]=gBM(S_T[i-1,j-1],sigma,r,T/Steps,random.gauss(0,1))
plt(S_T[:,Steps])
plt.show
