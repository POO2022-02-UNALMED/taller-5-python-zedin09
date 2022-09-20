class Zona:
    _zoo = [0]

    def __init__(self, nombre):
        self._nombre = nombre
        self._animales = []

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)
