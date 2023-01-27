# Definición de una función 
def data_personal():
    #Definicion de Variables 
    name = input('Ingrese su nombre: ')
    last_name = input('Ingrese su apellido: ')
    age = input('Ingrese su edad: ')

    full_name = [ name, last_name, age ]

    print(f'Nombre Completo: {full_name}\nEdad: {age}')

# Función con retorno y parametros 
def sum(a, b):
    return a + b

# LLamar funciones 
data_personal()

print(f'La suma: {sum(10, 30)}')