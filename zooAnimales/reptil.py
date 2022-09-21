from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitad, genero, colorEscamas, largoCola):
        super().__init__(self, nombre, edad, habitad, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls._listado.append(iguana)
        cls.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls._listado.append(serpiente)
        cls.serpientes += 1
        return serpiente

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getIguanas(cls):
        return cls.iguanas

    @classmethod
    def setIguanas(cls, iguanas):
        cls.iguanas = iguanas

    @classmethod
    def getSerpientes(cls):
        return cls.serpientes

    @classmethod
    def setSerpientes(cls, serpientes):
        cls.serpientes = serpientes

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

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largo):
        self._largoCola = largo






