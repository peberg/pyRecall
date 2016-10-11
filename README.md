# pyRecall
Speed up repeated function executions in Python 3 by caching pickle dumps.


```python
import numpy as np
import pyRecall as pr

inMat = np.random.rand(2000,2000)

@pr.pyRecall(verbose_timeit = True)
def slow_func(inMat):
    '''Return determinant'''
    return np.linalg.det(inMat)

#First call
slow_func(inMat)
>>> Execution time: 130.9 ms

#Second call can revert back to cache
slow_func(inMat)
>>> Execution time: 0.22 ms
```

##Installation
``` sh
git clone https://github.com/peberg/pyRecall
python setup.py install
```
See also
 [functools.lru_cache](https://docs.python.org/3/library/functools.html)
