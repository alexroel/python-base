#Definicion de Diccionario 
datos = {
    'uno':1,
    2:'Dos',
    'colores' : ['Rojo', 'Negro', 'Verde']
}

#Acceder asus dato mediante clave 
print(datos['colores'])

#Modificar datos 
datos['uno'] = 'Uno'
print(datos)

#Agregar datos 
datos['estado'] = True
print(datos)

#Eliminar
del(datos['uno'])
print(datos)

# Opter cada elementos 
print(datos.items())

# Obterner valores 
print(datos.values())

# Obtener Claves 
print(datos.keys())
