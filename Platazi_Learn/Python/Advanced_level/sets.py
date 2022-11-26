def run():
    set_1 = {1, 2, 3, 4}
    set_2 = {3, 4, 5, 6}
    set_3 = set_1.union(set_2)
    set_4 = set_1.symmetric_difference(set_2)
    set_5 = set_1.difference(set_2)
    set_6 = set_2.difference(set_1)
    set_7 = set_1.intersection(set_2)
    print(f'set 1: {set_1}')
    print(f'set 2: {set_2}') 
    print(f'Union: {set_3}')
    print(f'Symetric: {set_4}')
    print(f'Diference: {set_5}')
    print(f'Inversed diference: {set_6}')
    print(f'Intersection: {set_7}')

if __name__ == '__main__':
    run()