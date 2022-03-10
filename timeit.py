import time


def calculate_time(f):
    def wrap():
        start = time.time()
        f()
        end = time.time()
        print('Total time ', end - start)
    return wrap


def test():
    time.sleep(5)


test = calculate_time(test)
test()
