# a pow x
x = 2
a = 3

wynik = 1
while x > 0:
    if x % 2 == 1:
        wynik *= a
    a = a * a
    x = x // 2
print(wynik)