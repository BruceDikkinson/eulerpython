def is_palindrom(num):
    number = str(num)
    return number == number[::-1]


result = 0

for i in range(0, 999):
    for j in range(0, 999):
        num = i * j
        if is_palindrom(num) and num > result:
            result = num

print(result)
