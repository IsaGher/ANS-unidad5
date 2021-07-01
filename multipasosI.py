import sympy as sym
import pandas as pd

class MultiPasos:
    #inicializa datos necesarios, metodo inicializador, metodo predictor, metodo corrector, funcion, valores de x,y iniciales, valor de x a llegar, valor del espaciado, niveles
    def __init__(self,mInicializador,mPredictor,mCorrector,f,xo,yo,xlim,espaciado,n):
        self.inicializador = mInicializador
        self.predictor = mPredictor
        self.corrector = mCorrector
        self.funcion = f
        self.xo = xo
        self.yo = yo
        self.x = xlim
        self.h = espaciado
        self.n = n
    #evalua la funcion en x,y
    def evalF(tn,yn,f):
        x = sym.Symbol("x")
        y = sym.Symbol("y")
        p = sym.lambdify(x,f)
        ev = p(tn)
        p = sym.lambdify(y,ev)
        value = p(yn)
        return value
    #aquí estan todos los metodos inicializadores, predictores y correctores
    def multipasos(self):
        f = self.funcion
        funcion = sym.parse_expr(f)
        xo = self.xo
        yo = self.yo
        xfinal = self.x
        h = self.h
        n = self.n
        if n>0 and xo<xfinal and h>0:
            if type(n)==int:
                indiceI = self.inicializador
                indiceP = self.predictor
                indiceC = self.corrector
                #se evalua en algun metodo inicial
                #metodo de euler modificado
                if indiceI==1:
                    tn = [xo]
                    yn = [yo]
                    yi = ["---"]
                    #aplicacion del metodo,  tn es para x, yn es para y, yi son los valores para el refinamiento del metodo
                    for i in range(0,n-1):
                        temp = yn[i]+(h*MultiPasos.evalF(tn[i],yn[i],funcion))
                        yi.append(temp)
                        aux = tn[i]+h
                        tn.append(aux)
                        temp = yn[i]+h*((MultiPasos.evalF(tn[i],yn[i],funcion)+MultiPasos.evalF(tn[i+1],yi[i+1],funcion))/2)
                        yn.append(temp)
                    print("Multipasos\nMetodo inicial: Euler Modificado")
                #metodo de runge-kutta de cuarto orden
                elif indiceI==2:
                    tn = [xo]
                    yn = [yo]
                    #aplicacion del metodo,  tn es para x, yn es para y, k1 k2 k3 son las constantes
                    for i in range(0,n-1):
                        k1 = MultiPasos.evalF(tn[i],yn[i],funcion)
                        k2 = MultiPasos.evalF((tn[i]+h/2),(yn[i]+k1*(h/2)),funcion)
                        k3 = MultiPasos.evalF((tn[i]+h/2),(yn[i]+k2*(h/2)),funcion)
                        k4 = MultiPasos.evalF((tn[i]+h),(yn[i]+h*k3),funcion)
                        yn.append(yn[i]+(h/6)*(k1+2*k2+2*k3+k4))
                        tn.append(tn[i]+h)
                    print("Multipasos\nMetodo inicial: Runge-Kutta de cuarto orden")
                #se evalua en algun metodo predictor de Adams Bashforth
                #metodo de dos pasos
                if indiceP==1:
                    n = len(tn)
                    fi = list()
                    for i in range(0,n):
                        fi.append(MultiPasos.evalF(tn[i],yn[i],funcion))
                    y2 = yn[n-1]+(h/2)*(3*fi[n-1]-fi[n-2])
                    tn.append(tn[n-1]+h)
                    fi.append(MultiPasos.evalF(tn[n],y2,funcion))
                    yn.append(y2)
                    print("Metodo predictor: Adams Bashforth de dos pasos")
                #metodo de tres pasos
                elif indiceP==2:
                    n = len(tn)
                    fi = list()
                    for i in range(0,n):
                        fi.append(MultiPasos.evalF(tn[i],yn[i],funcion))
                    y3 = yn[n-1]+(h/12)*(23*fi[n-1]-16*fi[n-2]+5*fi[n-3])
                    tn.append(tn[n-1]+h)
                    fi.append(MultiPasos.evalF(tn[n],y3,funcion))
                    yn.append(y3)
                    print("Metodo predictor: Adams Bashforth de tres pasos")
                #metodo de cuatro pasos
                elif indiceP==3:
                    n = len(tn)
                    fi = list()
                    for i in range(0,n):
                        fi.append(MultiPasos.evalF(tn[i],yn[i],funcion))
                    y4 = yn[n-1]+(h/24)*(55*fi[n-1]-59*fi[n-2]+37*fi[n-3]-9*fi[n-4])
                    tn.append(tn[n-1]+h)
                    fi.append(MultiPasos.evalF(tn[n],y4,funcion))
                    yn.append(y4)
                    print("Metodo predictor: Adams Bashforth de cuatro pasos")
                #se evalua en algun metodo corrector de Adams Moulton
                #de un paso
                if indiceC==1:
                    i = len(yn)-1
                    n = len(fi)-1
                    y = yn[i-1]+(h/2)*(fi[n]+fi[n-1])
                    print("Metodo corrector: Adams Moulton de un paso")
                #de tres pasos
                if indiceC==2:
                    i = len(yn)-1
                    n = len(fi)-1
                    y = yn[i-1]+(h/24)*(9*fi[n]+19*fi[n-1]-5*fi[n-2]+fi[n-3])
                    print("Metodo corrector: Adams Moulton de tres pasos")
                #de cuatro pasos
                elif indiceC==3:
                    i = len(yn)-1
                    n = len(fi)-1
                    y = yn[i]+(h/720)*(251*fi[n]+646*fi[n-1]-254*fi[n-2]+106*fi[n-3]-19*fi[n-4])
                    print("Metodo corrector: Adams Moulton de cuatro pasos")
        
                t = {"xi":tn,"yi":yn,"fi":fi}
                tabla = pd.DataFrame(t)
                predictor = fi[n]
                print("Valor metodo predictor",predictor,"\nValor metodo corrector",y)
                return tabla
            else:
                error = "El valor de nivel tiene que ser un entero"
                return error
        else:
            error = "Datos introducidos de manera erronea"
            return error
