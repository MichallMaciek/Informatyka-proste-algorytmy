def wartosc(x):
    temp = 0
    for i, j in enumerate(f[::-1]):
        temp += j * x ** i
    return temp


def Wv2():
    a, b = przedzial
    if wartosc(a) * wartosc(b) > 0:
        raise ValueError("Funkcja musi mieć różne znaki na krańcach przedziału [a, b].")
    i = 0
    while abs(a - b) > przyblizenie and i < 50:
        x = (a+b) / 2
        if wartosc(x) == 0:
            return x
        if wartosc(x) * wartosc(a) < 0:
            b = x
        else:
            a = x
        i += 1
    return (a+b) / 2


przedzial = [-1, 4]
przyblizenie = 0.000001
#   x^2 +4x -5
f = [1, 4, -5]

print(Wv2())
