def divisors(num):
    try:
        if num < 0:
            raise ValueError("Solo se adminten Numeros positivos")

        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        return ve

def run():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisors(num))
        print("Termino el programa")
    except ValueError as ve:
        print("Solo se adminten Numeros")

if __name__ == '__main__':
    run()