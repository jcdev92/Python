from datetime import datetime

def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        time_elapsed = end_time - start_time
        print(f'function time wasted {time_elapsed.total_seconds()} seconds \n')
    return wrapper

@time_counter
def random_function():
    for _ in range(1,1000000):
        pass
    print('iteration cycle 1 to 1000000')

@time_counter
def sum(a: int, b:int) -> int:
    print(f'function sum result = {a + b}')

@time_counter
def grettings(name="name"):
    print('greetings function said: hello ' + name)

@time_counter
def run():
    random_function()
    sum(4,16)
    grettings('Pablo')
    print('Global time funtions')

if __name__ == '__main__':
    run()