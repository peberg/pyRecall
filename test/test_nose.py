#run "nosetests test --verbose" from cd ..
#or "nosetests test --verbose --with-coverage --cover-erase --cover-package=test"
import numpy as np

def test_numbers_3_4():
    assert np.multiply(3,4) == 12

def test_numbers_2s_4():
    assert 2+2+2+2+2+2 == 12
