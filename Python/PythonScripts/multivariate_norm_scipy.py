from scipy.stats import mvn
import numpy as np
low=np.array([-10000,-10000])
upp = np.array([0.1, -0.2])
mu = np.array([-0.3, 0.17])
S = np.array([[1.2,0.35],[0.35,2.1]])
mvn.mvnun(low,upp,mu,S)

#Memo
from scipy.stats import mvn
import numpy as np
low = np.array([-10, -10])
low_inf=np.array([-np.inf,-np.inf])
low_inf2=np.array([-100,-100])
low_inf3=np.array([-np.inf,-100])
low_inf4=np.array([-10000,-10000])
upp = np.array([.1, -.2])
mu = np.array([-.3, .17])
S = np.array([[1.2,.35],[.35,2.1]])
prob= mvn.mvnun(low_inf,upp,mu,S)
mvn.mvnun(low_inf2,upp,mu,S)
mvn.mvnun(low_inf3,upp,mu,S)
mvn.mvnun(low_inf4,upp,mu,S)#いける！！！！！

http://stackoverflow.com/questions/30560176/multivariate-normal-cdf-in-python-using-scipy
