def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    poblacion_paises = {
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 50372424  
    }
    # ciclo para recorrer el diccionario y obtener las llaves del diccionario.
    for pais in poblacion_paises.keys():
        print(pais)

    # ciclo para recorrer el diccionario y obtener los valores del diccionario
    for pais in poblacion_paises.values():
        print(pais)
    
    # ciclo para recorrer el diccionario y obtener los 2 opciones llaves y valores del diccionario
    for pais, poblacion in poblacion_paises.items():
        print(f' {pais} tiene {poblacion} habitantes')


if __name__ == '__main__':
    run()