from pyRecall import pyRecall
#from pyRecall import forgetRecalls

@pyRecall(timer=True)
def slow_func():
    print('asdf')
    return 'some output'

#Delete preceding funcRecall archives

slow_func()

from pyRecall import pyRecall, forgetRecalls
forgetRecalls()