#   x^2+2x+1
f = [1, 2, 1]    # <- funkcja kwadratowa
x = -1   #   <- podaj argument dla funkcji

wartosc = 0
for i in range(len(f)):
    wartosc = wartosc + f[::-1][i]*x**i

print(wartosc)