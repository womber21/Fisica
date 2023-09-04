import scipy.constants as cons
import numpy    as np
import matplotlib.pyplot as plt
lmin, lmax = 1,100
nmin, nmax = 1,100
n= np.linspace(nmin,nmax,100)
x = np.linspace(lmin, lmax, 100)
a=np.multiply(n,x)
e=cons.h*a
fig = plt.figure()
ax = fig.add_subplot(111, facecolor='k')
ax.plot(e,  c='w', lw=2)
ax.set_xlim(250,1000)
ax.set_ylim(-2,2)
plt.show()
