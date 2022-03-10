def decorador(func):
    def envolt(texto):
        return func(texto).upper()
    return envolt

@decorador
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

def run():
    print(mensaje('Cesar'))

if __name__ == '__main__':
    run()