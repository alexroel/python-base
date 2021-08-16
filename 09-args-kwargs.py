#Argumentos por posición 
def sumar (*args):
    print(args)
    suma = 0
    for n in args:
        suma += n

    print('Suma: ',suma)

sumar(4,5,6,8,7)

#Argumentos por nombre
def datos(nombre, **kwargs):
    print(nombre, kwargs)

datos(nombre = 'Alex', edad=26, estado = True) 
