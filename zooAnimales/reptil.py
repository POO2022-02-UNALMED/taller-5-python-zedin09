import animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitad, genero, colorEscamas, largoCola):
        super().__init__(self, nombre, edad, habitad, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    @staticmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @staticmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls._listado.append(iguana)
        cls.iguanas += 1
        return iguana

    @staticmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls._listado.append(serpiente)
        cls.serpientes += 1
        return serpiente

    @staticmethod
    def getListado(cls):
        return cls._listado

    @staticmethod
    def setListado(cls, listado):
        cls._listado = listado

    @staticmethod
    def getIguanas(cls):
        return cls.iguanas

    @staticmethod
    def setIguanas(cls, iguanas):
        cls.iguanas = iguanas

    @staticmethod
    def getSerpientes(cls):
        return cls.serpientes

    @staticmethod
    def setSerpientes(cls, serpientes):
        cls.serpientes = serpientes

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largo):
        self._largoCola = largo






