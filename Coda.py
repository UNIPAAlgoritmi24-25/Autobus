import Liste

class Lista:
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
            self.fine = self.fine.successore

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

l = Lista()

print(l.coda_vuota())
l.aggiungi("x")
l.aggiungi("y")
print(l.coda_vuota())
print(l.rimuovi())
print(l.rimuovi())