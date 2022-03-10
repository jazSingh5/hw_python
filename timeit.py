import time


def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        y = time.time()
        print('Total time: ', x - y)
    return wrapper
