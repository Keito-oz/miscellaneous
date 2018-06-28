import numpy as np
import matplotlib.pyplot as plt
mean = [0, 0]
cov = [[1, 0], [0, 100]]
x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()

mean = [0, 0, 0]
cov = [[1, 0, 0], [0, 100, 0], [0, 0, 20]]
x1, x2, x3 = np.random.multivariate_normal(mean, cov, 5000).T
len(x1)
plt.plot(x1)
plt.show()

#http://www.gpif.go.jp/operation/state/pdf/h27_q4.pdf
asset_names=["国内債券","国内株式","外国債券","外国株式"]
returns=[1.5,4.7,3.1,5.8]#国内債券、株式、外国債券、株式
stds=[4.2,25.23,11.82,26.78]
cov=[[1.0,-0.23,-0.04,-0.09],
     [-0.23,1,0.06,0.66,0.1],
     [-0.04,0.06,1.0,0.55,0.09],
     [-0.09,0.66,0.55,1,0.11],
     [0.2,0.1,0.09,0.11,1]]

plt.scatter(returns,stds)
plt.annotate(asset_names)
plt.show()

