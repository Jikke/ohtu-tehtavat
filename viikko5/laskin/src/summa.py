class Summa:
    def __init__(self, sovelluslogiikka, _lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = _lue_syote

    def suorita(self):
        self._sovelluslogiikka.plus(int(self._lue_syote()))