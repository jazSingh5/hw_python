from functools import wraps
import time

def calculate_time(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print ('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

@calculate_time
def f(a):
    for _ in range(a):
        i = 0
    return -1
