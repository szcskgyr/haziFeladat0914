# 11. Adott két pozitív szám, melyek 50 és 150 közöttiek.
# Írd ki a két változót a nevükkel és értékükkel együtt,
# majd cseréld meg a tartalmukat és újra írasd ki őket!

import beolvas
import math
import random

szam1 =  random.randint(50,150)
szam2 =  random.randint(50,150)

print("A két véletlen szám:")
print(szam1, szam2)

szam1_ = szam1
szam1 = szam2
szam2 = szam1_

print("A két véletlen szám fordítva:")
print(szam1, szam2)