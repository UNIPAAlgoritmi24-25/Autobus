import Liste

class Coda:
    def __init__(self):
        self.inizio = None
        self.fine = None

    def coda_vuota(self):
        return self.inizio is None

    def aggiungi(self, x):
        nodo = Liste.NodoDoppio(x)
        if self.coda_vuota():
            self.inizio = self.fine = nodo
        else:
            self.fine.successore = nodo
            nodo.precedente = self.fine
            self.fine = nodo

    def rimuovi(self):
        if self.coda_vuota():
            return None

        x = self.inizio

        if self.inizio.successore:
            self.inizio = self.inizio.successore
            self.inizio.precedente = None
        else:
            self.inizio = self.fine = None
        return x.valore

    def stampa(self):
        inizio = self.inizio
        output = []
        while inizio:
            output.append(inizio.valore)
            inizio = inizio.successore
        return output
