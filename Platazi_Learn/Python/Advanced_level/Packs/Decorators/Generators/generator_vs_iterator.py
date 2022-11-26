from datetime import datetime

##        generator_vs_iterator
## COMPREHENSION VS GENERATOR TIMER
def list_range():
    entry = int(input('entry a number: '))
    return [x for x in range(0, entry+1)]
    

def list_comprehension(my_list):
    start_time = datetime.now()
    my_comprehension_list = [x**2 for x in my_list]
    end_time = datetime.now()
    time_elapsed = end_time - start_time
    print(my_comprehension_list, f'it took {time_elapsed.total_seconds()} seconds')

def list_generator(my_list):
    start_time = datetime.now()
    my_generator_list = (x**2 for x in my_list)
    end_time = datetime.now()
    time_elapsed = end_time - start_time
    for i in my_generator_list:
        print(i)
    print(f'it took {time_elapsed.total_seconds()} seconds')

def run():
    my_list = list_range()
    list_comprehension(my_list)
    list_generator(my_list)
    

if __name__ == '__main__':
    run()