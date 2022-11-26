##   TIMER DECORATOR
from datetime import datetime

class decorators:

    def timer(func):
        func()
        def wrapper():
            start_time = datetime.now()
            func()
            end_time = datetime.now()
            time_elapsed = end_time - start_time
            print(time_elapsed.total_seconds())
        return wrapper