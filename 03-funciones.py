#Definición de funciones 
def saludar(nombre):
    #print('Hola desde la Función!')
    print(f'Hola, {nombre} desde la función!')

#Función que retona valores 
def sumar(a, b):
    return a + b


#Entrada de datos 
nombre = input('Ingrese su nombre: ')
a = int(input('Ingrese N01: '))
b = int(input('Ingrese N01: '))

#Llamar las funciones 
saludar(nombre)

suma = sumar(a, b)

print(f'La suma de {a} + {b} = {suma}')
