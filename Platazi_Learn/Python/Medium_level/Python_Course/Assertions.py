def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        assert num>=0
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), 'No se admiten letras, ni caracteres especiales, ni numeros negativos, por favor ingrese un numero positivo'
    print(divisors(int(num)))
    print("\nTerminó mi programa")



if __name__ == '__main__':
    run()