import timeit, time
import numpy as np
import pyRecall as pr
import shutil


def clearPycache():
    try:
        shutil.rmtree(pr.__path__[0]+'/__pycache__')
    except:
        pass



if __name__ == '__main__':

    
    test1 = True
    test2 = True
    test3 = True
    test4 = True
    
    if test1:
        print('\nTest 1: Simplest test case')
        
        @pr.pyRecall()
        def slow_func():
            time.sleep(1)
            return 'Some output'
        
        #Delete preceding funcRecall archives
        pr.forgetRecalls()
        
        for run in ['FIRST', 'SECOND']:
            out = timeit.timeit("slow_func()", \
                                 setup="from __main__ import slow_func", \
                                 number=1)
            print('   Execution time on '+run+' call of slow_func(): '+ \
                  str(1000*np.around(out,decimals=4))+' ms')
            clearPycache()

            
    if test2:
        print('\nTest 2: Test on numpy object')
        
        @pr.pyRecall()
        def numpy_func1(inMat):
            return np.linalg.det(inMat)
        
        #Delete preceding funcRecall archives
        pr.forgetRecalls()
        
        inMat = np.random.rand(2000,2000)
        for run in ['FIRST', 'SECOND']:
            out = timeit.timeit("numpy_func1(inMat)", \
                                 setup="from __main__ import numpy_func1, inMat", \
                                 number=1)
            print('   Execution time on '+run+' call of numpy_func1(): '+ \
                  str(1000*np.around(out,decimals=4))+' ms')
            clearPycache()

            
    if test3:
        print('\nTest 3: Change in function code')
        
        @pr.pyRecall(verbose_pickleFile = True)
        def function():
            return 'George II.'
        function()
        
        @pr.pyRecall(verbose_pickleFile = True)
        def function():
            return 'George IV.'
        function()
        
        print('Output files must be different')

        
            
    if test4:
        print('\nTest 4: Change in function name')
        
        @pr.pyRecall(verbose_pickleFile = True)
        def function1():
            return 'George III.'
        function1()
        
        @pr.pyRecall(verbose_pickleFile = True)
        def function2():
            return 'George III.'
        function2()
        
        print('Output files must be different')

    