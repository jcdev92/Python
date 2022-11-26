def read():
    numbers=[]
    with open('./Archivo/numbers.txt', 'r', encoding='utf8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ['Facundo', 'pepe', 'miguel', 'armando', 'mario', 'rocío', 'josé']

    with open('./Archivo/names.txt', 'w', encoding='utf8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    read()
    write()

if __name__ == '__main__':
    run()