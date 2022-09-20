import animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitad, genero, colorEscamas, cantidadAletas):
        super().__init__(self, nombre, edad, habitad, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    @staticmethod
    def cantidadPeces(cls):
        return len(cls._listado)

    @staticmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls._listado.append(salmon)
        cls.salmones += 1
        return salmon

    @staticmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls._listado.append(bacalao)
        cls.bacalaos += 1
        return bacalao

    @staticmethod
    def getListado(cls):
        return cls._listado

    @staticmethod
    def setListado(cls, listado):
        cls._listado = listado

    @staticmethod
    def getSalmones(cls):
        return cls.salmones

    @staticmethod
    def setSalmones(cls, salmones):
        cls.salmones = salmones

    @staticmethod
    def getBacalaos(cls):
        return cls.bacalaos

    @staticmethod
    def setBacalaos(cls, Bacalaos):
        cls.bacalaos = Bacalaos

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidad):
        self._cantidadAletas = cantidad






