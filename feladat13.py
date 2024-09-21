# 13. Tárolj el 2 számot egy-egy változóba, ami egy téglalap két oldala.
# Írd ki a téglalap kerületét és területét!

import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

teglalap_kerulet = (szam1+szam2)*2
teglalap_terulet = szam1*szam2

print("A téglalap kerülete", teglalap_kerulet)
print("A téglalap területe", teglalap_terulet)