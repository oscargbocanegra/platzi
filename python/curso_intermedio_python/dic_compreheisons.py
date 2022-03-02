import math
def run():
    # my_dict = {}

    # for i in range(1,101):
    #     if i % 3 !=0:
    #         my_dict[i] = i ** 3
    
    # Reto: Crear un dictionary comprehension 
    # cuyas llaves sean los 1000 primeros numeros naturales con sus raices cuadradas como valores.
    my_dict = {i: round(math.sqrt(i),2) for i in range(1,101)}
    print(my_dict)

    



if __name__ == "__main__":
    run()