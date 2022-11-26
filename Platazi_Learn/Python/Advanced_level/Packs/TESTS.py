from datetime import datetime

class decorators:

    def timer(func):
        def wrapper():
            start_time = datetime.now()
            func()
            end_time = datetime.now()
            time_elapsed = end_time - start_time
            print(f'it took {time_elapsed.total_seconds()} seconds')
        return wrapper

    def square_generator(func):
        def wrapper():
            generator = (i**2 for i in func())
            for n in generator:
                print(n)
        return wrapper

    def square_list_comprehension(func):
        def wrapper():
            list_square = [i**2 for i in func()]
            print(list_square)
        return wrapper

class entries:
        
        @decorators.timer
        @decorators.square_list_comprehension
        def list_range():
            entry = int(input('\nIntroduce a number to make a squares list of each previus number: '))
            return [x for x in range(0, entry+1)]
        
        @decorators.timer
        @decorators.square_generator
        def nums_range():
            entry = int(input('\nIntroduce a number to count it, and shows squares of each previus number: '))
            return [x for x in range(0, entry+1)]

def run():
    entries.list_range()
    entries.nums_range()


if __name__ == '__main__':
    run()





##    def timer(func):
##        func()
##        def wrapper():
##            start_time = datetime.now()
##            func()
##            end_time = datetime.now()
##            time_elapsed = end_time - start_time
##            print(time_elapsed.total_seconds())
##        return wrapper
