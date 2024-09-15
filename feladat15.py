# 15. Tárolj el 3 számot egy-egy változóba!
# Írd ki a középső számot az értékük szerint összehasonlítva!

import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()
szam3 = beolvas.tortSzamBeolvas()

# egy sorban jelekkel

print("\nA megoldás jelekkel:")

print(szam1, end="")

if szam1 > szam2:
    print(" > ", end="")
elif szam1 < szam2:
    print(" < ", end="")
else:
    print(" = ", end="")

print(szam2, end="")

if szam2 > szam3:
    print(" > ", end="")
elif szam2 < szam3:
    print(" < ", end="")
else:
    print(" = ", end="")

print (szam3)

# szöveges megoldás

print("\nA megoldás szövegesen\nAz középső szám:", szam2)

if szam1 > szam2:
    print("Az első szám nagyobb, mint a középső")
elif szam1 < szam2:
    print("Az első szám kisebb, mint a középső")
else:
    print("Az első szám egyenlő a középsővel")

if szam3 > szam2:
    print("A harmadik szám nagyobb, mint a középső")
elif szam3 < szam2:
    print("A harmadik szám kisebb, mint a középső")
else:
    print("A harmadik szám egyenlő a középsővel")