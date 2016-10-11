#run "nosetests test --verbose" from cd ..
import numpy as np

def test_numbers_3_4():
    assert np.multiply(3,4) == 12

def test_numbers_2s_4():
    assert 2+2+2+2+2+2 == 12