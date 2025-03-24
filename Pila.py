import Liste

class Pila:
    def __init__(self):
        self.indice = None

    def pila_vuota(self):
        return self.indice is None

    def aggiungi(self, valore):
        print(f"Aggiungo {valore}")
        x = Liste.Nodo(valore)
        if self.pila_vuota():
            self.indice = x
        else:
            x.successore = self.indice
            self.indice = x

    def rimuovi(self):
        if self.pila_vuota():
            return None

        out = self.indice
        self.indice = self.indice.successore
        return out.valore
