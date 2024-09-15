# 18. Ments el egy számot szövegként egy változóba,
# majd egy másik változóba egy egész számot.
# Majd írd ki az összegüket.

import beolvas

print ("Adj meg egy számot!", end=" ")
szam1 = beolvas.szovegBeolvas()
szam2 = beolvas.egeszSzamBeolvas()

osszeg = float(szam1) + float(szam2)

print("A két szám összege", osszeg)