"""Tests for pyRecall"""
import shutil
import time
import numpy as np
from pyRecall import pyRecall, purgeRecalls
import pyRecall as pr


def clear_pycache():
    """Remove ___pycache___"""
    try:
        shutil.rmtree(pr.__path__[0]+'/__pycache__')
    except:
        pass



if __name__ == '__main__':

    test1 = True
    test2 = True
    test3 = True
    test4 = True
    test5 = True
    test6 = True
    test7 = True    

    if test1:
        print('\nTest 1: Simplest test case')

        @pyRecall(timer=True)
        def slow_func():
            time.sleep(1)
            return 'some output'

        #Delete preceding funcRecall archives
        purgeRecalls()

        slow_func()
        clear_pycache()
        slow_func()
        clear_pycache()

    if test2:
        print('\nTest 2: Test on numpy object')

        @pyRecall(timer=True)
        def numpy_func1(mat):
            """Return determinant"""
            return np.linalg.det(mat)

        #Delete preceding funcRecall archives
        purgeRecalls()

        mat = np.random.rand(2000, 2000)

        numpy_func1(mat)
        clear_pycache()
        numpy_func1(mat)
        clear_pycache()


    if test3:
        print('\nTest 3: Change in function code')

        @pyRecall(verbose_pickleFile=True)
        def function():
            return 'George II.'
        function()

        @pyRecall(verbose_pickleFile=True)
        def function():
            return 'George IV.'
        function()

        print('Output files must be different')



    if test4:
        print('\nTest 4: Change in function name')

        @pyRecall(verbose_pickleFile=True)
        def function1():
            return 'George III.'
        function1()

        @pyRecall(verbose_pickleFile=True)
        def function2():
            return 'George III.'
        function2()

        print('Output files must be different')


    if test5:
        print('\nTest 5: Everything remains the same')

        @pyRecall(verbose_pickleFile=True)
        def function3():
            return 'George III.'
        function3()

        @pyRecall(verbose_pickleFile=True)
        def function3():
            return 'George III.'
        function3()

        print('Output files must be different')

    if test6:
        print('\nTest 6: Test for README.md, part 1')
        #Delete preceding funcRecall archives
        purgeRecalls()

        #------Start ------>        
        import numpy as np
        from pyRecall import pyRecall
        
        mat = np.random.rand(2000, 2000)
        
        @pyRecall(timer=True)
        def slow_func(mat):
            """Compute determinant"""
            return np.linalg.det(mat)

        slow_func(mat)
        slow_func(mat)
        #<-------End----------

if test7:
        print('\nTest 7: Test for README.md, part 2')
        #Delete preceding funcRecall archives
        purgeRecalls()

        #------Start ------>        
        mat1 = np.random.rand(2000, 2000)
        mat2 = np.random.rand(2000, 2000)        

        slow_func(mat1)
        slow_func(mat2)
        slow_func(mat1)        
        #<-------End----------
