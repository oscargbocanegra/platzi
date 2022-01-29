def run():
    for contador in range(1000):
        if contador %2 != 0:
            continue
        print (contador)

    texto = input("Escribe un texto: ")
    
    for letra in texto:
        print (letra)
        if letra == "o":
            break

if __name__ == '__main__':
    run()