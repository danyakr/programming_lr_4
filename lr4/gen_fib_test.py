import pytest
from gen_fib import my_genn

def test_fibonacci_first_3_elements1():
    gen = my_genn()
    result = gen.send(3)
    assert result == [0, 1, 1]

def test_fibonacci_first_5_elements1():
    gen = my_genn()
    result = gen.send(5)
    assert result == [0, 1, 1, 2, 3]

def test_fibonacci_first_8_elements1():
    gen = my_genn()
    result = gen.send(8)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13]

@pytest.fixture
def fibonacci_gen():
    return my_genn()

def test_fibonacci_first_3_elements(fibonacci_gen):
    result = fibonacci_gen.send(3)
    assert result == [0, 1, 1], f"Expected [0, 1, 1], but got {result}"

def test_fibonacci_first_5_elements(fibonacci_gen):
    result = fibonacci_gen.send(5)
    assert result == [0, 1, 1, 2, 3], f"Expected [0, 1, 1, 2, 3], but got {result}"

def test_fibonacci_first_8_elements(fibonacci_gen):
    result = fibonacci_gen.send(8)
    assert result == [0, 1, 1, 2, 3, 5, 8, 13], f"Expected [0, 1, 1, 2, 3, 5, 8, 13], but got {result}"
