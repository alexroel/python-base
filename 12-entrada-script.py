import sys

def main():
    if len(sys.argv) == 3:
        texto = sys.argv[1]
        cantidad = int(sys.argv[2])

        for _ in range(0,cantidad):
            print(texto)
    else:
        print('Error, Ingrese los argumentos correctamente')
        print('Ejemplo: entrada_script.py "Texto" 5')

if __name__ == '__main__':
    main()