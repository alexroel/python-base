#Definición de Listas 
colores = ['Rojo', 'Negro', 'Verde']

print(colores)

#Sacar un elemento de la lista 
print(colores[1])

#Agregar elementos a listas 
colores.append('Azul')
print(colores)

#Editar elemento 
colores[1] = 'Blanco'
print(colores)

#Eliminar el ultimo elemento
colores.pop()
print(colores)

#Eliminar elemento de la lista 
colores.remove('Rojo')
print(colores)

#Revertir una lista
colores.reverse()
print(colores)

#Vonvertir a tupla 
colores = tuple(colores)
print(colores)

print(colores[0]) 

#Longitud de elemntos
print(len(colores))

