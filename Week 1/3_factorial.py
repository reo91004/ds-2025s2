# 25.09.10
# 2020039069 박용성

# 팩토리얼


def factorial_iter(n):
    result = 1
    for k in range(1, n + 1):
        result = result * k
    return result


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


factorial(5)
factorial_iter(5)
