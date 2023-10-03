from enum import Enum


class CarroCores(Enum):
    Vermelho = "vermelho"
    Azul = "azul"
    Preto = "preto"


class Carro:
    def __init__(self, cor: CarroCores):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor
