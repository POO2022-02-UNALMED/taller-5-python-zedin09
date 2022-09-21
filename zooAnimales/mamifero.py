from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre, edad, habitad, genero, pelaje, patas):
        super().__init__(self, nombre, edad, habitad, genero)
        self._pelaje = pelaje
        self._patas = patas

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls._listado.append(caballo)
        cls.caballos += 1
        return caballo

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls._listado.append(leon)
        cls.leones += 1
        return leon

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getCaballos(cls):
        return cls.caballos

    @classmethod
    def setCaballos(cls, caballos):
        cls.caballos = caballos

    @classmethod
    def getLeones(cls):
        return cls.leones

    @classmethod
    def setLeones(cls, leones):
        cls.leones = leones

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._pelaje

    def setPatas(self, patas):
        self._patas = patas






