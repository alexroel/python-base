#Creando la función decorador 
def decorador(func):
    def decorar(*args, **kwargs):
        print('Inicio la ejecución de la función', func.__name__)
        func(*args, **kwargs)
        print('Termina la ejecución de la función', func.__name__)
    
    return decorar


#decorando una función 
@decorador
def saludar(nombre):
    print('Hola', nombre)

@decorador
def sumar(a, b):
    suma = a + b
    print('La suma es: ', suma)

#Ejecutar mi funcion 
saludar('Alex')
sumar(10,20)