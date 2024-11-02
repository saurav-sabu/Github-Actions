from src.math_operation import *

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0 
    assert add(100,1) == 101


def test_sub():
    assert sub(-1,1) == -2
    assert sub(2,3) == -1
    assert sub(5,3) == 2
    
