from euler import Euler
from taylor import Taylor

#pru = Euler("y+2*x*exp(2*x)",0,1,3,3)
#print(pru.eulerAtras())

prue = Taylor("y-x",1,3,5,5,3)
print(prue.taylor())