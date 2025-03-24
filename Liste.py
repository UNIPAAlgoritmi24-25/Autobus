class Nodo:
    def __init__(self, valore, successore=None):
        self.valore = valore
        self.successore = successore


class NodoDoppio(Nodo):
    def __init__(self, valore, successore=None, precedente=None):
        super().__init__(valore, successore)
        self.precedente = precedente


class Lista:
    def __init__(self, circolare=True, doppia=False):
        self.circolare = circolare
        self.doppia = doppia
        if doppia:
            self.indice = NodoDoppio(None)
        else:
            self.indice = Nodo(None)

        if circolare:
            self.indice.successore = self.indice
            if doppia:
                self.indice.precedente = self.indice

    def aggiungi(self, valore):
        # Creiamo il nodo giusto in base al tipo di lista
        if self.doppia:
            nuovo_nodo = NodoDoppio(valore)
        else:
            nuovo_nodo = Nodo(valore)

        # Caso lista vuota (solo nodo sentinella)
        if self.indice.successore == self.indice:
            nuovo_nodo.successore = self.indice
            self.indice.successore = nuovo_nodo
            if self.doppia:
                nuovo_nodo.precedente = self.indice
                self.indice.precedente = nuovo_nodo
        else:
            # Inserimento in testa (dopo il nodo sentinella)
            nuovo_nodo.successore = self.indice.successore
            self.indice.successore = nuovo_nodo

            if self.doppia:
                nuovo_nodo.precedente = self.indice
                nuovo_nodo.successore.precedente = nuovo_nodo

    def scansiona(self):
        corrente = self.indice.successore
        while corrente and corrente != self.indice:
            print(corrente.valore)
            corrente = corrente.successore
