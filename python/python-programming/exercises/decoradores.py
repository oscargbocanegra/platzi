def funcion_decorator(function_param):
    def function_inter():
        #Acciones adicionales que decorange
        print("Vamos a realizar un calculo")
        function_param()
        #Acciones adicionales que decorange
        print("Calculo terminado")
    return function_inter

@funcion_decorator
def suma():
    print(15+20)

@funcion_decorator
def resta():
    print(30-10)

suma()
resta()