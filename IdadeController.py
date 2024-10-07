from model.Idade import IdadeConverter

class IdadeController:
    def __init__(self):
        self._idade_converter = IdadeConverter()

    def validar_idade(self):
        if self._idade_converter.idade is None or self._idade_converter.idade < 0:
            raise ValueError("A idade não pode ser negativa ou nula.")

    def calcular_dias(self):
        self.validar_idade()
        return self._idade_converter.calcular_dias()

    def calcular_horas(self):
        self.validar_idade()
        return self._idade_converter.calcular_horas()

    def calcular_minutos(self):
        self.validar_idade()
        return self._idade_converter.calcular_minutos()

    def calcular_segundos(self):
        self.validar_idade()
        return self._idade_converter.calcular_segundos()

    @property
    def idade_converter(self):
        return self._idade_converter

    @idade_converter.setter
    def idade_converter(self, valor):
        self._idade_converter = valor
