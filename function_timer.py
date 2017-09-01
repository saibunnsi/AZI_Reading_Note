# coding:utf-8
import time
from functools import wraps

#使用装饰器来计算函数运行时间：
def deco_timer(func):
    @wraps(func)
    def func_timer(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()

        '''
        print("running %s : costs %s seconds" %
              (func.func_name, str(t1-t0))
              )
        '''
        return result, ('running : {}'.format(func.__name__),
              'costs: {} seconds'.format(t1 - t0))
    return func_timer
