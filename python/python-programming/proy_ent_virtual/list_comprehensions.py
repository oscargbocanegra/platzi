def run():
    squares = []
    # for i in range(1,101):
    #     if i % 3 !=0:
    #         squares.append(i)

    #Con list compreheinsons
    #squares = [i**2 for i in range(1,101) if i % 3 !=0]

    # Crear un List compreheison de todos los multiplos de 4 que a la vez sean multiplos de 6 y 9 hasta 5 digitos.
    #squares = [i**2 for i in range(1,10001) if i % 4 !=0 & i % 6 !=0 & i % 9 !=0 ]
    squares = [i for i in range(1,10001) if i % 36 ==0 ]
    print(squares)

if __name__ == '__main__':
    run()