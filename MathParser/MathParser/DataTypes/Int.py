from numba import jit
@jit
def factor(num):
    output = []
    for x in range(1, num+1):
        if num%x == 0: output.append(num)
    return output
def factor_dict(num):
    output = {}
    for x in range (1, num+1):
        if num%x == 0: output.update({x:num/x})
    return output
def isPrime(num):
    if len(factor(num)) <= 2: return True
    else: return False
@jit
def test():
    for x in range(1, 100000):
        for y in range(1, 100000):
            x+y
    print("done")