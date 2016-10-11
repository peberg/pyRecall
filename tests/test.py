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
    test11 = True    
    test2 = True
    test3 = True
    test4 = True
    test5 = True    
    
    if test1:
        print('\nTest 1: Simplest test case')
        
        @pr.pyRecall(verbose_timeit = True)
        def slow_func():
            time.sleep(1)
            return 'Some output'
        
        #Delete preceding funcRecall archives
        pr.forgetRecalls()

        slow_func()
        clearPycache()          
        slow_func()       
        clearPycache()        
            
    if test2:
        print('\nTest 2: Test on numpy object')
        
        @pr.pyRecall(verbose_timeit = True)
        def numpy_func1(inMat):
            return np.linalg.det(inMat)
        
        #Delete preceding funcRecall archives
        pr.forgetRecalls()
        
        inMat = np.random.rand(2000,2000)
        
        numpy_func1(inMat)
        clearPycache()          
        numpy_func1(inMat)
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
        
            
    if test5:
        print('\nTest 5: Everything remains the same')
        
        @pr.pyRecall(verbose_pickleFile = True)
        def function3():
            return 'George III.'
        function3()
        
        @pr.pyRecall(verbose_pickleFile = True)
        def function3():
            return 'George III.'
        function3()
        
        print('Output files must be different')
    