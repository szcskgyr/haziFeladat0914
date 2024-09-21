# 12. Tárolj el egy egész számot egy változóba, ami egy kör átmérője.
# Írd ki a kör kerületét és területét!

import beolvas
import math

szam1 = beolvas.egeszSzamBeolvas()

kor_kerulet = szam1 * math.pi
kor_terulet = (szam1/2)**2 * math.pi


print("A kör kerülete", kor_kerulet)
print("A kör területe", kor_terulet)