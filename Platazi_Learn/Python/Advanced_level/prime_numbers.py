def is_prime(numbs:int) -> bool: 
    counter = 0
    for i in range(1, numbs+1):
        if i == 1 or i == numbs:
            continue
        if numbs%i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

def run():
    number = int(input('ingrese un numero: '))
    if is_prime(number):
        print(f'{number} ES PRIMO')
    else:
        print(f'{number} NO ES PRIMO')


if __name__ == '__main__':
    run()
