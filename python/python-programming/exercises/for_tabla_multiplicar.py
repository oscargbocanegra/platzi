def run():
    mensaje = """
    Bienvenidos a la seccion tablas de multiplicar con while
    """
    print (mensaje)

    for i in range(1,10):
        print (f' ****** Esta es la tabla del {i} ******')
        for j in range(1,10):
            print(f'Tabla de {i} por {j} = a {i*j}')

if __name__ == '__main__':
    run()