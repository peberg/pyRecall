# pyRecall
Speed up repeated function executions by pickling.

``` sh
import time
import pyRecall as pr

@pr.pyRecall(verbose_timeit = True)
def slow_func():
    time.sleep(1)

slow_func()
>>> Execution time: 1001.47 ms
slow_func()
>>> Execution time: 0.22 ms
```

##Installation
``` sh
git clone https://github.com/peberg/pyRecall
python setup.py install
```
 [functools.lru_cache](https://docs.python.org/3/library/functools.html)
