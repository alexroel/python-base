# Diccionarios 

~~~python
#Definicion de Diccionario 
data= {
    'uno':1,
    2:'Dos',
    'colores' : ['Rojo', 'Negro', 'Verde']
}

#Acceder asus dato mediante clave 
print(data['colores'])

#Modificar datos 
data['uno'] = 'Uno'
print(data)

#Agregar datos 
data['estado'] = True
print(data)

#Eliminar
del(data['uno'])
print(data)

# Opter cada elementos 
print(data.items())

# Obterner valores 
print(data.values())

# Obtener Claves 
print(data.keys())

~~~