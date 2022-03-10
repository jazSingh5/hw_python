import time


def calculate_time(f):
    def wrapper():
        start = time.time()
        f()
        finish = time.time()
        print('Total time ', finish - start)
    return wrapper


def test():
    time.sleep(3)


test = calculate_time(test)
test()
