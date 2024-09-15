# 17. Mentsd el egy változóba a vezetékneved, egy másikba a keresztneved,
# majd mentsd el a teljes nevedet egy teljesNev változóba, aztán írd ki!

import beolvas

print("Add meg a vezetékneved!", end=" ")
vezetekNev = beolvas.szovegBeolvas()

print("Add meg a keresztneved!", end=" ")
keresztNev = beolvas.szovegBeolvas()

teljesNev =  vezetekNev + " " + keresztNev

print("A teljes neved:", teljesNev)