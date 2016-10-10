import timeit, time
import numpy as np
from pyRecall import pyRecall, forgetRecalls
import shutil


if __name__ == '__main__':


    test1 = False#True
    test2 = True
    
    if test1:
        """Simplest test case"""
        
        @pyRecall
        def slow_func():
            time.sleep(2)
            return 'Some output'
        
        #Delete preceding funcRecall archives
        forgetRecalls()
        
        print('Test 1:')
        for run in ['FIRST', 'SECOND']:
            out = timeit.timeit("slow_func()", \
                                 setup="from __main__ import slow_func", \
                                 number=1)
            print('   Execution time on '+run+' call of slow_func(): '+ \
                  str(1000*np.around(out,decimals=4))+' ms')

    if test2:
        """Test on numpy object"""
        
        @pyRecall
        def numpy_func1(inMat):
            return np.linalg.det(inMat)
        
        #Delete preceding funcRecall archives
        forgetRecalls()
        
        print('Test 2:')
        inMat = np.random.rand(201,201)
        for run in ['FIRST', 'SECOND']:
            out = timeit.timeit("numpy_func1(inMat)", \
                                 setup="from __main__ import numpy_func1, inMat", \
                                 number=1)
            print('   Execution time on '+run+' call of numpy_func1(): '+ \
                  str(1000*np.around(out,decimals=4))+' ms')
            #shutil.rmtree('../__pycache')
        
        pass
    
    