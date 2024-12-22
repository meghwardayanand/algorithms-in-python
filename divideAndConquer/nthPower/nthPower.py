
# O(log(n))
def nthPowerOptimized(x, n):
    if n == 0:
        return 1

    half = nthPowerOptimized(x, n//2)
    if n % 2 == 0:
        return  half * half
    else:
        return half * half * x


# O(n)
def nthPowerNaive(x, n):
    result = 1
    for _ in range(n):
        result *= x

    return result
