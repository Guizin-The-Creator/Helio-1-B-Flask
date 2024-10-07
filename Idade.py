class IdadeConverter:
    def __init__(self):
        self._idade = None  # Inicializa a idade como None

    # Método para calcular o número de dias vividos
    def calcular_dias(self):
        if self._idade is not None:
            return self._idade * 365  # Considera 365 dias por ano
        else:
            return None

    # Método para calcular o número de horas vividas
    def calcular_horas(self):
        dias = self.calcular_dias()
        if dias is not None:
            return dias * 24
        else:
            return None

    # Método para calcular o número de minutos vividos
    def calcular_minutos(self):
        horas = self.calcular_horas()
        if horas is not None:
            return horas * 60
        else:
            return None

    # Método para calcular o número de segundos vividos
    def calcular_segundos(self):
        minutos = self.calcular_minutos()
        if minutos is not None:
            return minutos * 60
        else:
            return None

    # Getter para idade
    @property
    def idade(self):
        return self._idade

    # Setter para idade
    @idade.setter
    def idade(self, value):
        if value < 0:
            raise ValueError("A idade não pode ser negativa.")
        self._idade = value
