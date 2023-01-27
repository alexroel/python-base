# Clases y Objetos 

~~~python
# Clases y Objetos 

class Cracker:
    #Constructor 
    def __init__(self, name, flavor, color) -> None:
        self.name = name
        self.flavor = flavor
        self.color = color

    #Métodos    
    def imprimer(self):
        datos = f"""
        Nombre: {self.name}
        Sabor: {self.flavor}
        Color: {self.color}
        """
        print(datos)
    

    #Estado del Objeto 
    def __str__(self) -> str:
        return f'Galletas:({self.nombre} {self.sabor} {self.color})'

#Crear el Objeto
cracker1 = Cracker('Oreo', 'Dulce', 'Negro')
cracker2 = Cracker('Ritz', 'Salado', 'Dorado')

#Obtener un elemento del objeto 
print(cracker1.nombre)

#ejecutar metodos 
cracker1.imprimer()
cracker2.imprimer()

#Editar datos 
cracker1.color = 'Naranjado'
cracker2.imprimer()

#Estado de Objeto 
print(cracker1, cracker2)


#Herencia 
class Soda(Cracker):
    pass

#Crear objetos de sub clase 
soda1 = Soda('Coca Cola', 'Dulce', 'Negro')

soda1.imprimer()

print(soda1)
~~~