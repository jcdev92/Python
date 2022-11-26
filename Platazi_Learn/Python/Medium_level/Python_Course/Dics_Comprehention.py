import math

def run():

#    nature_nums = {i:i**3 for i in range(1,101) if i%3 != 0}
#    print(nature_nums)

    nature_roots = {i: math.sqrt(i) for i in range(1,1001) if math.sqrt(i)%2 == 0} # Dictionary of natural numbers for keys and integer squares of themselves for values.
    print(nature_roots)


if __name__ == '__main__':
    run()