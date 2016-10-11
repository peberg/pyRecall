# pyRecall
Speed up repeated function executions (in Python 3) by dumping/loading pickle files.
[![Build Status](https://travis-ci.org/peberg/pyRecall.png)](https://travis-ci.org/peberg/pyRecall)


```python
import numpy as np
import pyRecall as pr

mat = np.random.rand(2000, 2000)

@pr.pyRecall(timer=True)
def slow_func(mat):
    """Compute determinant"""
    return np.linalg.det(mat)

#Initial call
slow_func(mat)
>>> Execution time: 130.9 ms

#Repeat call reverts to cache
slow_func(mat)
>>> Execution time: 0.2 ms
```

##Installation
``` sh
git clone https://github.com/peberg/pyRecall
python setup.py install
```
See also
 [functools.lru_cache](https://docs.python.org/3/library/functools.html)
