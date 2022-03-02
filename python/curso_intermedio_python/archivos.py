def read():
    numbers = []
    with open("./archivos/numbers.txt", 'r', encoding='utf8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Luis", "Sara", "Adrian", "Christian", "Rocío", "David"]
    
    #Modo de sobre escritura en el archivo.
    #with open("./archivos/names.txt", 'w', encoding='utf8') as f:
    #Modo de adicion en el archivo.
    with open("./archivos/names.txt", 'a', encoding='utf8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    #read()
    write()

if __name__ == '__main__':
    run()