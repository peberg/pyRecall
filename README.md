# pyRecall
Speed up repeated function executions (in Python 3) by dumping/reloading pickle files.
[![Build Status](https://travis-ci.org/peberg/pyRecall.png)](https://travis-ci.org/peberg/pyRecall)


```python
import numpy as np
import pyRecall as pr

mat = np.random.rand(2000, 2000)

@pr.pyRecall(verbose_timeit=True)
def slow_func(mat):
    """Return determinant"""
    return np.linalg.det(mat)

#First call
slow_func(mat)
>>> Execution time: 130.9 ms

#Second call can revert to cache
slow_func(mat)
>>> Execution time: 0.22 ms
```

##Installation
``` sh
git clone https://github.com/peberg/pyRecall
python setup.py install
```
See also
 [functools.lru_cache](https://docs.python.org/3/library/functools.html)
