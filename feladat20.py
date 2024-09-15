# 20. Ments el két törtszámot két változóba,
# add össze őket, majd írd ki egészre kerekített értéküket!

import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

szamKerekitve = round(szam1 + szam2)

print("A két szám összege egészre kerekítve:", szamKerekitve)