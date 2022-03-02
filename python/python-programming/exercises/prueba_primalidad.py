def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
            print(f' {numero} % {i} = 0 {numero % i == 0} ')
        else:
            print(f' {numero} % {i} = 0 {numero % i == 0} ')
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input("Escribe un numero: "))
    primo = es_primo(numero)
    if primo:
        print(f' {primo} Es primo')
    else:
        print(f' {primo} NO Es primo')

if __name__ == '__main__':
    run()