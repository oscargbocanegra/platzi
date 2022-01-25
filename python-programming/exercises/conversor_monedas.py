menu = """
Bienvenidos al conversor de monedas 🪙 💴
1 - Pesos colombianos
2 - Pesos Argentinos.
3 - Pesos Mexicanos
Elige una opción: """

option = int(input(menu))

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    divisa = round(pesos / valor_dolar,2)
    print("Tienes $" + str(divisa) + " dolares")
    #return divisa

if option == 1:
    conversor("Colombianos", 3875)

elif option == 2:
    conversor("Argentinos", 65)

elif option == 3:
    conversor("Mexicanos", 24)

else:
    print("Ingress una option correcta")
