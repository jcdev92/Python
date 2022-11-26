### DECORTATOR
def capitalize(func):
    def wrapped(text):
        return func(text).upper()
    return wrapped

@capitalize
def message(name):
    return f'{name}, you have a pending message'

def run():
    print(message('cesar'))

if __name__ == '__main__':
    run()