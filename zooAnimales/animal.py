from anfibio import *
from ave import *
from mamifero import *
from pez import *
from reptil import *

class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitad, genero, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitad = habitad
        self._genero = genero
        self._zona = zona

    @staticmethod
    def movimiento(cls):
        return "desplazarse"

    @staticmethod
    def totalPorTipo(cls):
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
