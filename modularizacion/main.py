#from mate import sumar, restar
from mate import *

from geometry.figures import Cuadrado as cua

def main():
    sumar(4,5)
    restar(10,5)

    c1 = cua(8)
    print(c1.area())
    print(c1.perimetro())

if __name__ == '__main__':
    main()