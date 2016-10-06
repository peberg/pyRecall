import timeit, time
import numpy as np
from funcRecall import funcRecall

@funcRecall
def slow_func():
    time.sleep(2)
    return 'Some output'

if __name__ == '__main__':

    for run in ['FIRST','SECOND']:
        out = timeit.timeit("slow_func()", setup="from __main__ import slow_func", number=1)
        print('Execution time on '+run+' call of slow_func(): '+ \
              str(1000*np.around(out,decimals=5))+' ms')

