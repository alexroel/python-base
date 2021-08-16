# Clases y Objetos 

class Galleta:
    #Constructor 
    def __init__(self, nombre, sabor, color) -> None:
        self.nombre = nombre
        self.sabor = sabor
        self.color = color

    #Métodos    
    def imprimer(self):
        datos = f"""
        Nombre: {self.nombre}
        Sabor: {self.sabor}
        Color: {self.color}
        """
        print(datos)
    

    #Estado del Objeto 
    def __str__(self) -> str:
        return f'Galletas:({self.nombre} {self.sabor} {self.color})'

#Crear el Objeto
galleta1 = Galleta('Oreo', 'Dulce', 'Negro')
galleta2 = Galleta('Ritz', 'Salado', 'Dorado')

#Obtener un elemento del objeto 
print(galleta1.nombre)

#ejecutar metodos 
galleta1.imprimer()
galleta2.imprimer()

#Editar datos 
galleta2.color = 'Naranjado'
galleta2.imprimer()

#Estado de Objeto 
print(galleta1, galleta2)


#Herencia 
class Gaseosa(Galleta):
    pass

#Crear objetos de sub clase 
gaseosa1 = Gaseosa('Coca Cola', 'Dulce', 'Negro')

gaseosa1.imprimer()

print(gaseosa1)



