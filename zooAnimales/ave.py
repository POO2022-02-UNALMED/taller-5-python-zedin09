from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitad, genero, colorPlumas):
        super().__init__(self, nombre, edad, habitad, genero)
        self._colorPlumas = colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls._listado.append(halcon)
        cls.halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls._listado.append(aguila)
        cls.aguilas += 1
        return aguila

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado

    @classmethod
    def getHalcones(cls):
        return cls.halcones

    @classmethod
    def setHalcones(cls, halcones):
        cls.halcones = halcones

    @classmethod
    def getAguilas(cls):
        return cls.aguilas

    @classmethod
    def setAguilas(cls, aguilas):
        cls.aguilas = aguilas

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

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color):
        self._colorPlumas = color






