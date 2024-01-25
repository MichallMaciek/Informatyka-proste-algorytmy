NormalPow = lambda a, x: a**x


def BinPow(a, x):
    temp = 1
    for i, j in enumerate(bin(x)[2:][::-1]):
        if j == '1':
            temp *= a**(i+1)
    return temp


def Binaary_Xiation(a, x):
    result = 1
    while x > 0:
        if x % 2 == 1:
            result *= a
        a *= a
        x //= 2
    return result


print(NormalPow(3, 4))
print(Binaary_Xiation(5, 5))
print(BinPow(3, 3))
