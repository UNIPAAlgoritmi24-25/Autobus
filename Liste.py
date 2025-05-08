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

    def aggiungi_in_coda(self, valore):
        if self.doppia:
            nuovo = NodoDoppio(valore)
        else:
            nuovo = Nodo(valore)

        # Lista vuota (solo sentinella)
        if self.indice.successore is None or self.indice.successore == self.indice:
            nuovo.successore = self.indice if self.circolare else None
            self.indice.successore = nuovo
            if self.doppia:
                nuovo.precedente = self.indice
                if self.circolare:
                    self.indice.precedente = nuovo
        else:
            corrente = self.indice
            while corrente.successore != self.indice and corrente.successore is not None:
                corrente = corrente.successore
            corrente.successore = nuovo
            nuovo.successore = self.indice if self.circolare else None
            if self.doppia:
                nuovo.precedente = corrente
                if self.circolare:
                    self.indice.precedente = nuovo

    def scansiona(self):
        corrente = self.indice.successore
        while corrente and corrente != self.indice:
            print(f"{corrente.valore}", end=" --> ")
            corrente = corrente.successore
        print("Ø")

    def stampa(self):
        output = []
        corrente = self.indice.successore
        while corrente and corrente != self.indice:
            output.append(corrente.valore)
            corrente = corrente.successore
        print(output)