from functools import reduce

def run():
    # FUNCTION ANONYMOUS -- LAMBDA   

    palindrome = lambda string: string == string[::-1]
    print(palindrome('ana'))
    
    ## FUNCIONES DE ORDEN SUPERIOR
    
    # FUNCTION FILTER 

    my_list = [1,4,5,6,9,13,19,21]

    odd = list(filter(lambda x: x%2 != 0, my_list))
    print(odd)

    #FUNCTION MAP
    numbers = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, numbers))
    print(squares)

    # FUNCTION REDUCE

    twos = [2,2,2,2,2]
    reduces = reduce(lambda a, b: a * b, twos)
    print(reduces)

if __name__ == '__main__':
    run()

