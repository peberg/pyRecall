# pyRecall [![Build Status](https://travis-ci.org/peberg/pyRecall.png)](https://travis-ci.org/peberg/pyRecall) [![codecov.io](https://codecov.io/gh/peberg/pyRecall/branch/master/graphs/badge.svg)](https://codecov.io/gh/peberg/pyRecall/branch/master)

Emulate make/cmake/[SCons](https://docs.python.org/3/library/functools.html) functionality within python code through function decorators. pyRecall can save computation time after kernel restarts or when functions are called repetitively.
```python
import numpy as np
from pyRecall import recall

mat = np.random.rand(2000, 2000)

@recall(timer=True)
def slow_func(mat):
    """Compute determinant"""
    return np.linalg.det(mat)

#Initial call
slow_func(mat)
>>> Execution time: 130.9 ms

#Repetitive call reverts to return of initial call
slow_func(mat)
>>> Execution time: 0.2 ms
```
pyRecall uses adaptive pickling/unpickling of function returns and hashing, and is thereby not limited to the most recent function call (similar to [functools.lru_cache](https://docs.python.org/3/library/functools.html)).
```python
mat1 = np.random.rand(2000, 2000)
mat2 = np.random.rand(2000, 2000)        

slow_func(mat1)
>>> Execution time: 108.1 ms
slow_func(mat2)
>>> Execution time: 104.1 ms
slow_func(mat1)
>>> Execution time: 0.1 ms
```
Since the hashing is also taking the function code into account, pyRecall is compliant with code changes.

Clearing pyRecall's history works as follows
```python
from pyRecall import purgeRecalls
purgeRecalls()
```


##Installation
In case, Python3 is standard
``` sh
git clone https://github.com/peberg/pyRecall
python setup.py install
```
otherwise
``` sh
python3 setup.py install
```

