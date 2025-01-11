import functools
import itertools
import pytest

def fib_elem_gen():
    """Генератор, возвращающий элементы ряда Фибоначчи"""
    a = 0
    b = 1

    while True:
        yield a
        res = a + b
        a = b
        b = res

def my_genn():
    """Функция, которая возвращает первые n элементов ряда Фибоначчи."""
    while True:
        number_of_fib_elem = yield  
        fib_gen = fib_elem_gen()  
        l = list(itertools.islice(fib_gen, number_of_fib_elem))  
        yield l  

def fib_coroutine(g):
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        gen.send(None)  
        return gen
    return inner

my_genn = fib_coroutine(my_genn)

@pytest.fixture
def fib_gen_fixture():
    """Фикстура, создающая экземпляр сопрограммы fib_coroutine."""
    return my_genn()

def test_fib_elem_gen():
    """Тест для генератора fib_elem_gen."""
    fib_gen = fib_elem_gen()
    expected_fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, expected in zip(range(10), expected_fib):
        assert next(fib_gen) == expected

def test_my_genn_basic():
     """Тест для сопрограммы my_genn с отправкой значений."""
     gen = my_genn()
     assert gen.send(3) == [0, 1, 1]
     assert gen.send(5) == [0, 1, 1, 2, 3]
     assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_my_genn_fixture(fib_gen_fixture):
    """Тест для функции my_genn, использующий фикстуру."""
    assert fib_gen_fixture.send(3) == [0, 1, 1]
    assert fib_gen_fixture.send(5) == [0, 1, 1, 2, 3]
    assert fib_gen_fixture.send(8) == [0, 1, 1, 2, 3, 5, 8, 13]

def test_my_genn_zero_elements():
    """Тест для сопрограммы my_genn с запросом нуля элементов."""
    gen = my_genn()
    assert gen.send(0) == []
