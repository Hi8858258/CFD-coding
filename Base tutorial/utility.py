from time import time

#time装饰
def timer(func):
    def func_wrapper(*args, **kwarge):
        time_start = time()
        result = func(*args, **kwarge)
        time_end = time()
        time_spend = time_end - time_start
        print('\n{0} cost time {1} s\n'.format(func.__name__, time_spend))
        return result
    return func_wrapper