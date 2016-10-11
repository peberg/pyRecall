# pyRecall [![Build Status](https://travis-ci.org/peberg/pyRecall.png)](https://travis-ci.org/peberg/pyRecall)

Emulate the capabilities of make/cmake or  [SCons](https://docs.python.org/3/library/functools.html) through function decorators, i.e. save computation time by accelerating repetitive function executions. pyRecall uses adaptive pickling/unpickling of function returns and hashing, and is thereby not limited to the most function recent call (see [functools.lru_cache](https://docs.python.org/3/library/functools.html)).
```python
import numpy as np
from pyRecall import pyRecall

mat = np.random.rand(2000, 2000)

@pyRecall(timer=True)
def slow_func(mat):
    """Compute determinant"""
    return np.linalg.det(mat)

#Initial call
slow_func(mat)
>>> Execution time: 130.9 ms

#Repetitive call reverts to pickle
slow_func(mat)
>>> Execution time: 0.2 ms
```

##Installation
``` sh
git clone https://github.com/peberg/pyRecall
python setup.py install
```
