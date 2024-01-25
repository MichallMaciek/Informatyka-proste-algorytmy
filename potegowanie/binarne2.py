# a pow x
x = 2
a = 3

xbinarnie = bin(x)[2:][::-1]
wynik = 1
for i in range(len(xbinarnie)):
    if xbinarnie[i] == "1":
        wynik *= a**(i+1)
print(wynik)
