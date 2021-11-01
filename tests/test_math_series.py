from math_series import __version__
from math_series.math_series import lucas
from math_series.math_series import fibonacci
from math_series.math_series import sum_series



def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci0():
    actual = fibonacci(0)
    expected=0
    assert actual == expected


def test_fibonacci3():
    actual = fibonacci(3)
    expected=2
    assert actual == expected    



def test_lucas():
    actual = lucas(0)
    expected=2
    assert actual == expected


def test_lucas1():
    actual = lucas(1)
    expected=1
    assert actual == expected



def test_lucas5():
    actual = lucas(5)
    expected=11
    assert actual == expected



def test_sum_seriesN5():
    actual = sum_series(-5)
    expected="Cant do sum series on negative num"
    assert actual == expected    


def test_sum_series0():
    actual = sum_series(0)
    expected=0
    assert actual == expected    
def test_sum_series1():
    actual = sum_series(1)
    expected=1
    assert actual == expected    

def test_sum_series2():
    actual = sum_series(2,5,5)
    expected=10
    assert actual == expected    


   
