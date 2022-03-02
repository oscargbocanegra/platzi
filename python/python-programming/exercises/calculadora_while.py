def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    return a/b

def run():
    opcion = int(input("""
    Bienvenidos a la calculadora con while escoja la tarea a ejecutar
    1 - Suma
    2 - Resta
    3 - multiplicación
    4 - División
    5 - Salir
    
    Ingrese Opcion: """))

    if opcion > 4:
        print(f'Opcion No valida')
    else:
        while opcion <= 4:
            a = int(input("Ingrese el primer valor: "))
            b = int(input("Ingrese el segundovalor: "))

            if opcion == 1:
                print(f'El resultado de la suma {a} + {b} es {suma(a,b)}')
                break
            if opcion == 2:
                print(f'El resultado de la resta {a} - {b} es {resta(a,b)}')
                break
            if opcion == 3:
                print(f'El resultado de la Multiplicacion {a} * {b} es {multiplica(a,b)}')
                break
            if opcion == 4:
                print(f'El resultado de la Divisiòn {a} / {b} es {divide(a,b)}')
                break

if __name__ == '__main__':
    run()