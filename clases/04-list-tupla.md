# Listas y Tuplas 

~~~python
#Definición de Listas 
colors = ['Rojo', 'Negro', 'Verde']

print(colors)

#Sacar un elemento de la lista 
print(colors[1])

#Agregar elementos a listas 
colors.append('Azul')
print(colors)

#Editar elemento 
colors[1] = 'Blanco'
print(colors)

#Eliminar el ultimo elemento
colors.pop()
print(colors)

#Eliminar elemento de la lista 
colors.remove('Rojo')
print(colors)

#Revertir una lista
colors.reverse()
print(colors)

#Vonvertir a tupla 
colores = tuple(colors)
print(colores)

print(colores[0]) 

#Longitud de elemntos
print(len(colores))
~~~