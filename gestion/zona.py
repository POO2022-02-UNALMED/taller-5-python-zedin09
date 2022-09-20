class Zona:

    def __init__(self, nombre, animales, zoo):
        self._nombre = nombre
        self._animales = animales
        self._zoo = zoo

    def agregarAnimales(self, animal):
        self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self._animales)

#comentario innecesario