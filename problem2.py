prevFibonacci = 0
fibonacci = 1
temp = 0

result = 0

while True:
    temp = fibonacci
    fibonacci += prevFibonacci
    prevFibonacci = temp
    if fibonacci < 4000000:
        if fibonacci % 2 == 0:
            result += fibonacci
    else:
        break
print(result)
