import animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitad, genero, pelaje, patas):
        super().__init__(self, nombre, edad, habitad, genero)
        self._pelaje = pelaje
        self._patas = patas

    @staticmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @staticmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls._listado.append(caballo)
        cls.caballos += 1
        return caballo

    @staticmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls._listado.append(leon)
        cls.leones += 1
        return leon

    @staticmethod
    def getListado(cls):
        return cls._listado

    @staticmethod
    def setListado(cls, listado):
        cls._listado = listado

    @staticmethod
    def getCaballos(cls):
        return cls.caballos

    @staticmethod
    def setCaballos(cls, caballos):
        cls.caballos = caballos

    @staticmethod
    def getLeones(cls):
        return cls.leones

    @staticmethod
    def setLeones(cls, leones):
        cls.leones = leones

    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._pelaje

    def setPatas(self, patas):
        self._patas = patas






