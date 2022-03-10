def list_iterator():
    my_list = [1,2,3,4,5]
    my_iter = iter(my_list)
    for element in my_iter:
        print(element)

def run():
    list_iterator()

if __name__ == '__main__':
    run()
