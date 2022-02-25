def palindromo(palabra):
    try:
        if len(palabra) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        else:
            palabra = palabra.replace(' ', '')
            palabra = palabra.lower()
            palabra_invertida = palabra[::-1]
            palabra == palabra_invertida
        return True

    except ValueError as ve:
        print(ve)
        return False

def run():
    palabra = input('Escribe una palabra: ')
    #palabra = 1
    try:
        es_palindromo = palindromo(palabra)
        if es_palindromo == True:
            print('Es palindromo:')
        else:
            print('No es palindromo:')
    except TypeError:
        print('Solo se pueden ingresar Strings')

if __name__ == '__main__':
    run()