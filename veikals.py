class Veikals:
    _darbinieki: 'list[Darbinieks]'
    _telpa: 'Telpa'
    def __init__(self) -> None:
        self._darbinieki = []
    def AprekinatDarbiniekuAlgas(self) -> float:
        algas = 0.0
        for darbinieks in self._darbinieki:
            algas += darbinieks.IzvaditAlgu()
        return algas
    def PirktProduktus(self, klients: 'Klients') -> 'list[Produkts]':
        kasieris = None
        for darbinieks in self._darbinieki:
            if type(darbinieks) == kasieris:
                kasieris = darbinieks
                break
        if kasieris == None:
            print("Nav pieejams kasieris!")
        else:
            kasieris._aiznemts = True

class Darbinieks:
    _alga: float = 100.0
    def IzvaditAlgu(self):
        return self._alga
class Menedzeris(Darbinieks):
    _alga = 2000.0
class Pavars(Darbinieks):
    _alga = 400.0
class Kravejss(Darbinieks):
    _alga = 500.0
class Pakotajs(Darbinieks):
    _alga = 600.0
class Apsargs(Darbinieks):
    _naudaparnoķeršanu: float
    def __init__(self) -> None:
        self._alga = 150.0
        self._dzeramnauda = 0.0
    def IzvaditAlgu(self):
        return super().IzvaditAlgu() + self._dzeramnauda
class Kasieris(Darbinieks):
    _aiznemts: bool
    def __init__(self) -> None:
        self._alga = 700.0
        self._aiznemts = False
    def IzvaditAlgu(self):
        return super().IzvaditAlgu() + self._dzeramnauda
class Preces:
    _izmaksas: float
    _daudzums: float
    _cena: float
    def __init__(self, izmaksas: float, daudzums: float, cena: float) -> None:
        self._izmaksas = izmaksas
        self._daudzums = daudzums
        self._cena = cena
    def IzvaditIzmaksas(self) -> float:
        return self._izmaksas*self._daudzums    
class Virtuve:
    _preces: 'list[prece]'
    def __init__(self) -> None:
        self._preces = []
class Klients:
    _nauda: float    