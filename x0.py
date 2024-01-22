def Wv2():
    a = przedzial[0]
    b = przedzial[1]
    if wartosc(a) * wartosc(b) > 0:
        raise ValueError("Funkcja musi mieć różne znaki na krańcach przedziału [a, b].")
    i = 0
    while abs(a-b) > eps and i < 100:
        x = (a+b)/2
        if wartosc(x) == 0:
            return x
        elif wartosc(x) * wartosc(a) < 0:
            b = x
        else:
            a = x
        i += 1
    return (a+b)/2


def wartosc(x):
    temp = 0
    for i in range(len(f)-1):
        temp += f[i]*x**(len(f)-i-1)
    return temp + f[-1]

przedzial = [-10, 10]
eps = 0.001
#   x^3x^2+2x+1
f = [1, 1, 2, 1]

print(Wv2())