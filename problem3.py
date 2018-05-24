def divideByPrime(num, n):
    num = num / n
    if num % n == 0:
        num = divideByPrime(num, n)
    return num


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:

        print
        '\t', f
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


num = 600851475143;

for x in range(2, num):
    if is_prime(x) and num % x == 0:
        print(x)
        num = divideByPrime(num, x)

    if num < x:
        break

print(x)
