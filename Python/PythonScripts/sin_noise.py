def sin(x,T=100):
    return np.sin(2.0+np.pi*x/T)

def toy_problem(T=100,ampl=0.05):
    x=np.arange(0,2*T+1)
    noise=ampl*np.random.uniform(low=-1.0,high=1.0,size=len(x))
    return sin(x)+noise

T=100
f=toy_problem(T)

plt.plot(f)
plt.show()
