from euler import Euler
from taylor import Taylor
from runge import Runge

#pru = Euler("y+2*x*exp(2*x)",0,1,3,3)
#print(pru.eulerAtras())

#prue = Taylor("cos(x)+y",0,1,3,6,4)
#print(prue.taylor())

prue = Runge("2*x*y",0,1,0.5,5)
print(prue.rungeCuatro())