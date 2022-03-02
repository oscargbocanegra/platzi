import random

def generate_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracter = MAYUS + MINUS + NUMS + CHARS
    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracter)
        contrasena.append(caracter_random)
    
    # Opcion para covertir la lista en un string
    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generate_contrasena()
    print(f'Tu nueva contraseña es: {contrasena} ')


if __name__ == '__main__':
    run()