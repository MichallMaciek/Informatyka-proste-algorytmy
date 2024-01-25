from math import log10
def s(x):
    eps = 1e-10
    y, xx = 1, x
    while abs(x-y) > eps:
        x = (x+y)/2
        y = xx/x
    return round(x, int(log10(round(eps**(-1)))))
print(s(4))
