# 14. Tárolj el 3 számot egy-egy változóba!
# Írd ki a számtani közepüket!

import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()
szam3 = beolvas.tortSzamBeolvas()

szamtani_kozep = (szam1 + szam2 + szam3) / 3

print("A három szám számtani közepe:", szamtani_kozep)