import time
from functools import wraps


def calculate_time(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        tl = ts-te
        print('Total time took: %2.4f sec' %
              (f.__name__, args, kw, tl))
        return result
    return wrap
