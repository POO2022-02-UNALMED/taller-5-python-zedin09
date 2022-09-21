from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(self, nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "humedal", genero, "rojo", True)
        cls._listado.append(rana)
        cls.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "jungla", genero, "negro y amarillo", False)
        cls._listado.append(salamandra)
        cls.salamandras += 1
        return salamandra

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getRanas(cls):
        return cls.ranas

    @classmethod
    def setRanas(cls, ranas):
        cls.ranas = ranas

    @classmethod
    def getSalamandras(cls):
        return cls.salamandras

    @classmethod
    def setSalamandras(cls, salamandras):
        cls.salamandras = salamandras

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

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso






