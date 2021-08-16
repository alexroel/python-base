
#Crear una función de Cierre
def can_repetir(n: int):
    def repetir(c: str):
        return c * n

    return repetir

#Probar closure
repetir2 = can_repetir(2)
print(repetir2('Hola'))
print(repetir2('Mundo'))

repetir3 = can_repetir(3)
print(repetir3('Alex'))