def prime_divisors(number):
    "return list of prime divisors for natural number"

    if number < 1:
        return []

    result = []
    current = 2

    while current * current <= number:
        while number % current == 0:
            result.append(current)
            number /= current
        current += 1

    if number != 1:
        result.append(number)

    if len(result) < 1:
        result = [number]

    return result

def single_test(number, divisors):
    "single unit test for prime_divisors function"
    res = 1
    for div in divisors:
        res *= div
    return res == number

def test_prime_divisors():
    "unit tests for prime_divisors function"

    assert single_test(100, prime_divisors(100))
    assert single_test(49, prime_divisors(49))
    assert single_test(12321, prime_divisors(12321))
    assert single_test(123456789, prime_divisors(123456789))
    assert single_test(1, prime_divisors(1))

    print "all tests passed"
    return

test_prime_divisors()