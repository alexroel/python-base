#Definicion de Variables 
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = input('Ingrese su edad: ')

#Imprimer los datos
#print('Nombre:', nombre)
#print('Apellido:', apellido)
#print('Edad:', edad)

nombre_completo = f'{nombre} {apellido}'

print(f'Nombre Completo: {nombre_completo}\nEdad: {edad}')
