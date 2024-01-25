def ff(x):
    temp = 0
    for i, j in enumerate(f[::-1]):
        temp += j*x**i
    return temp
#   x^2+2x+1
f = [1, 2, 1]

print(ff(-1))
