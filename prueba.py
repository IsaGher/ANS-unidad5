from euler import Euler
from taylor import Taylor
from runge import Runge
from multipasosI import MultiPasos

#Aquí se pueden elegir entre cuatro opciones, euler hacia adelante (eulerAdelante), euler hacia atras (eulerAtras), euler centrado (eulerCentrada) y euler modificado (eulerModificado)
#Se ingresa f que es la funcion, xo que es el valor de x donde se inicia, yo es el valor inicial de y
#Ejemplo, en y(0)=1, xo es 0, yo es 1
#xlim es el valor de x donde se termina de iterar, por ejemplo dan solo y(0.8) = ?, xlim es 0.8
#intervalo(puede aparecer en los problemas como n) es el numero de divisiones que tendra el intervalo de x(xo) inicial hasta la x final (xlim), este sera solo numeros enteros, pueda que el problema ya lo de o se deba de calcular
#para calcular h, (xlim-xo)/n, a la x final se le resta la x inicial, luego a esto se le divide el numero de intervalos que se crearan o sea n
#para calcular n, (xlim-xo)/h, a la x final se le resta la x inicial, luego a esto de le divide el espaciado o sea h
pru = Euler("2*x*y",4,5,6,4)
print(pru.eulerAdelante())


#Este metodo solo funciona si y aparece como independiente en la ecuacion y que sea positivo, no tiene que aparecer multiplicando o dividiendo o dentro de una funcion
#Se ingresa f que es la funcion, xo que es el valor de x donde se inicia, yo es el valor inicial de y
#Ejemplo, en y(0)=1, xo es 0, yo es 1
#xlim es el valor de x donde se termina de iterar, por ejemplo dan solo y(0.8) = ?, xlim es 0.8
#intervalo(puede aparecer en los problemas como n) es el numero de divisiones que tendra el intervalo de x(xo) inicial hasta la x final (xlim), este sera solo numeros enteros, pueda que el problema ya lo de o se deba de calcular
#orden es hasta que derivada se va a calcular, solo acepta enteros de 2 en adelante
#para calcular h, (xlim-xo)/n, a la x final se le resta la x inicial, luego a esto se le divide el numero de intervalos que se crearan o sea n
#para calcular n, (xlim-xo)/h, a la x final se le resta la x inicial, luego a esto de le divide el espaciado o sea h
prue = Taylor("y-x**2",0,2,1,2,2)
print(prue.taylor())

#Aquí se pueden elegir entre tres opciones, runge de segundo orden (rungeDos), runge de tercer orden (rungeTres) y runge de cuarto orden (rungeCuatro)
#Se ingresa f que es la funcion, xo que es el valor de x donde se inicia, yo es el valor inicial de y
#Ejemplo, en y(0)=1, xo es 0, yo es 1
#xlim es el valor de x donde se termina de iterar, por ejemplo dan solo y(0.8) = ?, xlim es 0.8
#intervalo(puede aparecer en los problemas como n) es el numero de divisiones que tendra el intervalo de x(xo) inicial hasta la x final (xlim), este sera solo numeros enteros, pueda que el problema ya lo de o se deba de calcular
#para calcular h, (xlim-xo)/n, a la x final se le resta la x inicial, luego a esto se le divide el numero de intervalos que se crearan o sea n
#para calcular n, (xlim-xo)/h, a la x final se le resta la x inicial, luego a esto de le divide el espaciado o sea h
prue = Runge("2*x*y",0,1,0.5,5)
print(prue.rungeCuatro())


#Para multipasos primero se elige el metodo inicial, esta Euler Modificado(1) y Runge-Kutta de cuarto orden(2)
#Luego se elije el metodo predictor, para este caso estan los de Adams Bashforth de dos pasos(1), de tres pasos(2) y de cuatro pasos(3)
#Sigue el metodo corrector donde estan los de Adams Moulton de un paso(1), de tres pasos(2) y de cuatro pasos(3)
#Luego se ingresa f que es la funcion, xo que es el valor de x donde se inicia, yo es el valor inicial de y
#Ejemplo, en y(0)=1, xo es 0, yo es 1
#xlim es el valor de x donde se termina de iterar, por ejemplo dan solo y(0.8) = ?, xlim es 0.8
#h es el espaciado, puede ser entero o decimal, puede que el problema ya lo de o se deba de calcular
#n es el numero de divisiones que tendra el intervalo de x(xo) inicial hasta la x final (xlim), este sera solo numeros enteros, pueda que el problema ya lo de o se deba de calcular
#para calcular h, (xlim-xo)/n, a la x final se le resta la x inicial, luego a esto se le divide el numero de intervalos que se crearan o sea n
#para calcular n, (xlim-xo)/h, a la x final se le resta la x inicial, luego a esto de le divide el espaciado o sea h
prue = MultiPasos(2,3,2,"x+y-1",0,1,0.8,0.2,4)
print(prue.multipasos())


