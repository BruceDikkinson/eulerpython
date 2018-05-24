import math

def log(x, base):
    return (int)(math.log(x) / math.log(base))


def recursiveLogStar(n, b):

    if n > 1.0:
        return 1.0 + recursiveLogStar(log(n, b), b)
    else:
        return 0


n = 10000000000000
base = 2

print(recursiveLogStar(n, base))

print(math.log(recursiveLogStar(n, base)))
print(recursiveLogStar(math.log(n), base))

