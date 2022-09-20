class Zoologico:

    def __init__(self, nombre, ubicacion, zonas):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    def agregarZona(self, zona):
        self._zonas.append(zona)

    def cantidadTotalAnimales(self):
        cont = 0
        for zona in self._zonas:
            cont += len(zona)
        return cont




