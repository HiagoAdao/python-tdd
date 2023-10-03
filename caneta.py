class Caneta:
    def __init__(self, cor: str):
        self.__cor = cor
        self.__validar()

    @property
    def cor(self):
        return self.__cor

    def __validar(self):
        if not self.cor:
            raise ValueError("A caneta está inválida")
