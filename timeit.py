from time import time
from functools import wraps


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('Total time took: %2.4f sec' %
              (f.__name__, args, kw, te-ts))
        return result
    return wrap
