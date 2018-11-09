from e1 import Euler_1
from e2 import Euler_2
from e3 import Euler_3
from e4 import Euler_4
from e5 import Euler_5
from e18 import Euler_18
from e22 import Euler_22

def test_1():
    assert Euler_1() == 233168

def test_2():
    assert Euler_2() == 4613732

def test_3():
    assert Euler_3() == 6857

def test_4():
    assert Euler_4() == 906609

def test_5():
    assert Euler_5() == 232792560

def test_18():
    assert Euler_18() == 1074

def test_22():
    assert Euler_22() == 871198282