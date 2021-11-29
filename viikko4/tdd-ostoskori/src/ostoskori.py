from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self._ostokset.values():
            maara += ostos.lukumaara()
        return maara 
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset.values():
            hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        nimi = ostos.tuotteen_nimi()
        if nimi in self._ostokset.keys():
            maara = ostos.lukumaara()
            self._ostokset[nimi].muuta_lukumaaraa(maara)
        else:
            self._ostokset[nimi] = ostos
    

    def poista_tuote(self, poistettava: Tuote):
        poistettavan_nimi = poistettava.nimi()
        if poistettavan_nimi in self._ostokset.keys():
            self._ostokset[poistettavan_nimi].muuta_lukumaaraa(-1)
            if self._ostokset[poistettavan_nimi].lukumaara() == 0:
                del self._ostokset[poistettavan_nimi]

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset = []
        for ostos in self._ostokset.values():
            ostokset.append(ostos)
        return ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
