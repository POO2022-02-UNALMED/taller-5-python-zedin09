


class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitad, genero, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitad = habitad
        self._genero = genero
        self._zona = zona

    @classmethod
    def movimiento(cls):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return "Mamiferos: " + Mamifero.cantidadMamiferos() + '\n' + \
               "Aves: " + Ave.cantidadAves() + '\n' + \
               "Reptiles: " + Reptil.cantidadReptiles() + '\n' + \
               "Peces: " + Pez.cantidadPeces() + '\n' + \
               "Anfibios: " + Anfibio.cantidadAnfibios()

    def __str__(self):
        if self._zona is None:
            return "Mi nombre es " + self._nombre + \
                   ", tengo una edad de " + self._edad + \
                   ", habito en " + self._habitad + \
                   " y mi genero es " + self._genero
        else:
            return "Mi nombre es " + self._nombre + \
                   ", tengo una edad de " + self._edad + \
                   ", habito en " + self._habitad + \
                   " y mi genero es " + self._genero + \
                   ", la zona en la que me ubico es " + self._zona + \
                   ", en el " + self._zona.zoo
