import numpy as np
import pylab as pl

# Efecto Fotoelectrico
Vf=[[0.1432],[0.168],[0.775]]
v=[[5.19*10**14],[5.5*10**14],[5.88*10**14]]
regr = linear_model.LinearRegression()
regr.fit(Vf,v)
print('Coefficients: \n', regr.coef_, regr.intercept_)
pl.figure(1)
pl.plot(Vf, regr.predict(Vf), color='black', linewidth=3)
pl.scatter(Vf, v, s=40, marker='o', color='r')
pl.xlabel('Frecuencia (Hz)')
pl.ylabel('Voltaje Frenado (V)')
pl.tittle('Caracteristica filtro Amarillo',fontsize = 17, color = 'k', verticalalignment = 'baseline', horizontalalignment = 'center')
pl.xlim(.0, 1.0)
pl.ylim(.0, 1.5)
pl.show()