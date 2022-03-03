def es_primo(int: int) -> bool:
    result_list = [x for x in range(2, int+1) if int % x == 0]
    res_final = len(result_list) == 1
    if res_final == True:
        print(f'{int} es primo')
    else:
        print(f'{int} NO es primo')

def run():
    numero = int(input("Escribe un numero: "))
    es_primo(numero)

if __name__ == '__main__':
    run()