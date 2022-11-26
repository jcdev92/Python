def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("\nInserte solo numeros positivos")
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return "vuelva a intentarlo"


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("\nTerminó mi programa")
    except ValueError:
        print("No se admiten letras o carcateres espciales, por favor, ingrese un numero")



if __name__ == '__main__':
    run()