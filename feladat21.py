# 21. Ments el két törtszámot két változóba,
# vondd ki őket, majd írd ki egészre kerekített értéküket!

import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

szamKerekitve = round(szam1 - szam2)

print("A két szám különbsége egészre kerekítve:", szamKerekitve)