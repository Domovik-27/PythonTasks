"Implementation of some functions using generators"

def integers(value):
    "generates integer numbers in range [0;value)"
    for num in range(value):
        yield num

def check_integers(value):
    "single test of result for 'integers' generator"
    return list(integers(value)) == range(value)

def test_integers():
    "unit tests for 'integers' generator"
    assert check_integers(0)
    assert check_integers(100)
    assert check_integers(27)
    assert check_integers(-555)
    assert check_integers(1024)
    print "all tests for 'integers' passed"

test_integers()


def factr(value):
    "generates factorization of number"
    for pos_div in xrange(2, int(value ** 0.5) + 1):
        while value % pos_div == 0:
            yield pos_div
            value //= pos_div

    if 1 != value:
        yield value

def check_factr(value):
    "single test for 'factr' generator"
    divisors = list(factr(value))

    res = 1
    for div in divisors:
        res *= div
    return res == value

def test_factr():
    "unit tests for 'factr' generator"
    assert check_factr(100)
    assert check_factr(49)
    assert check_factr(12321)
    assert check_factr(123456789)
    assert check_factr(1)
    print "all tests for 'factr' passed"

test_factr()


def fibonacci_gen(value):
    "generator for Fibonacci sequence"
    first = 0
    second = 1

    yield first
    while second <= value:
        yield second

        second += first
        first = second - first

def fibonacci_func(value):
    "returns Fibonacci sequence"
    res = [0]
    cur = 1

    while cur <= value:
        res.append(cur)
        cur += res[-2]
    return res

def check_fibonacci_gen(value):
    "single test for 'fibonacci_gen' generator"
    return list(fibonacci_gen(value)) == fibonacci_func(value)

def test_fibonacci_gen():
    "unit tests for 'fibonacci_gen' generator"
    assert check_fibonacci_gen(0)
    assert check_fibonacci_gen(100)
    assert check_fibonacci_gen(27)
    assert check_fibonacci_gen(78)
    assert check_fibonacci_gen(10000)
    print "all tests for 'fibonacci_gen' passed"

test_fibonacci_gen()


def gen_filter(func, cont):
    "'filter' on generator"
    for i in cont:
        if func(i):
            yield i

def gen_reduce(func, gen):
    "'reduce' on generator"
    it = iter(gen)
    res = next(it)
    for i in it:
        res = func(res, i)
    return res