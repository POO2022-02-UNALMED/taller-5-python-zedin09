import animal


class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitad, genero, colorPlumas):
        super().__init__(self, nombre, edad, habitad, genero)
        self._colorPlumas = colorPlumas

    @staticmethod
    def cantidadAves(cls):
        return len(cls._listado)

    @staticmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls._listado.append(halcon)
        cls.halcones += 1
        return halcon

    @staticmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls._listado.append(aguila)
        cls.aguilas += 1
        return aguila

    @staticmethod
    def getListado(cls):
        return cls._listado

    @staticmethod
    def setListado(cls, listado):
        cls._listado = listado

    @staticmethod
    def getHalcones(cls):
        return cls.halcones

    @staticmethod
    def setHalcones(cls, halcones):
        cls.halcones = halcones

    @staticmethod
    def getAguilas(cls):
        return cls.aguilas

    @staticmethod
    def setAguilas(cls, aguilas):
        cls.aguilas = aguilas

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color):
        self._colorPlumas = color






