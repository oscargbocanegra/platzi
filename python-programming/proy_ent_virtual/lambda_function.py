def run():
    palindromo = lambda string: string == string[::-1]
    print(palindromo('ana'))

if __name__ == '__main__':
    run()