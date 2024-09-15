# 16. Tárolj el 2 számot egy-egy változóba, melyek egy derékszögű háromszög befogói.
# Mekkora a harmadik oldal?

import math
import beolvas

# befogók értékeinek beolvasása
befogo1 = beolvas.tortSzamBeolvas()
befogo2 = beolvas.tortSzamBeolvas()

# átfogó értéke Pythagorasz-tétel alapján
atfogo = math.sqrt( befogo1**2 + befogo2**2 )

# kiírás
print("A háromszög átfogója:", atfogo)