# 19. Tárolj el egy kétjegyű egész számot egy változóba!
# Írd ki a számjegyek összegét!

szam = input("Adj meg egy kétszámjegyű egész számot! ")

print("A két számjegy összege:", int(szam[:1]) + int(szam[1:]))

