import itertools

def is_evenly_divisible(num,max):
    for i in range(2,max):
        if num%i != 0:
            return False
    return True

max=20
for i in itertools.count(1,1):
    if(is_evenly_divisible(i,max)):
        print(i)
        break
