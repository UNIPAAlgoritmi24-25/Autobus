
class Nodo:
    def __init__(self, valore, successore = None):
        self.valore = valore
        self.successore = successore


class NodoDoppio(Nodo):
    def __init__(self, valore, successore=None, precedente=None):
        super().__init__(valore, successore)
        self.precedente = precedente


