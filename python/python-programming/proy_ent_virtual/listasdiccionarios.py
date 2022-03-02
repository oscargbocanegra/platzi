def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Oscar", "last name": "Hurtado"}

    super_list = [
        {"firstname": "Oscar", "lastname": "Hurtado"},
        {"firstname": "Facundo", "lastname": "Torres"},
        {"firstname": "Miguel", "lastname": "Lopez"},
        {"firstname": "Juan", "lastname": "Rodriguez"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2,3,4,5],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for values in super_list:
        print(values["firstname"], "-", values["lastname"])
        #print(values)

if __name__ == '__main__':
    run()