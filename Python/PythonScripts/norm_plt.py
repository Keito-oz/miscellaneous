import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import scipy.stats as stats
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-20, 20, 0.5)
X, Y = np.meshgrid(x, y)
mu = np.array([0,0])
sigma = np.array([[10,0],
                  [0,10]])
f = lambda x, y: stats.multivariate_normal(mu, sigma).pdf([x, y])
Z = np.vectorize(f)(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.show()
