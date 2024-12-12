import functools
import itertools

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
    """Сопрограмма, которая возвращает первые n элементов ряда Фибоначчи."""
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

if __name__ == "__main__":
    gen = my_genn()
    
    print(gen.send(3))
    print(gen.send(5))
    print(gen.send(8))  