def run():
    super_list = [
        {"first name: ": "Jesus", "last name: ": "Clemente"},
        {"first name: ": "Andres", "last name: ": "Ramirez"},
        {"first name: ": "Carlitos", "last name: ": "Duran"},
        {"first name: ": "Sara", "last name: ": "Taylor"}
    ]

    super_dict = {
        "Natural Nums: " : [1, 2, 3, 4, 5],
        "Integer Nums: " : [-2, -1, 0, 1, 2],
        "Float Nums: " : [4.3, 6.1, 2.2, 1.5]
    }

    for keys, values in super_dict.items():
        print(keys, values)

    print(" ")

    for n in super_list:
        print('')
        for k, v in n.items():
            print(k,v)

if __name__ == '__main__':
    run()