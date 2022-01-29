
def run():
    tabla = int(input("Introduce la tabla de multiplicación: "))
    contador = 0

    while contador <= 10:
        resultado = tabla*contador
        print(f' tabla de {tabla} por {contador} es Igual a {resultado}')
        contador = contador + 1

if __name__ == '__main__':
    run()