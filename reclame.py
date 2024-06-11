def aanbieding_1(smaak, prijs, korting):
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {(1-korting) * prijs} euro.")

print(aanbieding_1("aardbei", 4, 0.1))



def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    totaal_btw = totaal_inkomsten * btw
    print(f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten}, waarover {totaal_btw} euro btw betaald dient te worden")

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    lijst = [max(mijn_lijst),min(mijn_lijst)]
    return lijst

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    lijst = sum(mijn_lijst) / 7
    print(f"De gemiddlde inkomsten deze wijk zijn {lijst} euro")

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    global laag_en_hoog
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))