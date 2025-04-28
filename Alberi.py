# Definizione della classe Nodo
class Nodo:
    def __init__(self, etichetta, padre=None):
        self.etichetta = etichetta    # Valore del nodo
        self.padre = padre             # Nodo padre
        self.nodo_sinistro = None      # Figlio sinistro
        self.nodo_destro = None        # Figlio destro

    def ha_figli(self):
        """Restituisce True se il nodo ha almeno un figlio, False altrimenti."""
        return self.nodo_sinistro is not None or self.nodo_destro is not None

    def __str__(self):
        """Restituisce una rappresentazione testuale del nodo."""
        return str(self.etichetta)


# Definizione della classe Albero base
class Albero:
    def __init__(self):
        self.radice = None  # Inizialmente l'albero è vuoto

    def stampa(self, nodo=None, livello=1):
        """Stampa l'albero in modo visuale."""
        if nodo is None:
            nodo = self.radice
        if nodo is not None:
            prefisso = "    " * (livello - 1)
            prefisso += "└── " if livello != 1 else ""
            print(f"{prefisso}{nodo.etichetta}")
            if nodo.nodo_sinistro:
                self.stampa(nodo.nodo_sinistro, livello + 1)
            if nodo.nodo_destro:
                self.stampa(nodo.nodo_destro, livello + 1)


# Albero binario di ricerca (ordinato)
class AlberoOrdinato(Albero):
    def __init__(self):
        super().__init__()

    def aggiungi_nodo(self, valore):
        """Aggiunge un nodo all'albero mantenendo l'ordinamento."""
        nuovo_nodo = Nodo(valore)
        if self.radice is None:
            self.radice = nuovo_nodo
        else:
            self._inserisci(self.radice, nuovo_nodo)

    def _inserisci(self, corrente, nuovo_nodo):
        """Metodo interno ricorsivo per inserire un nodo."""
        if nuovo_nodo.etichetta < corrente.etichetta:
            if corrente.nodo_sinistro is None:
                corrente.nodo_sinistro = nuovo_nodo
                nuovo_nodo.padre = corrente
            else:
                self._inserisci(corrente.nodo_sinistro, nuovo_nodo)
        else:
            if corrente.nodo_destro is None:
                corrente.nodo_destro = nuovo_nodo
                nuovo_nodo.padre = corrente
            else:
                self._inserisci(corrente.nodo_destro, nuovo_nodo)

    def cerca(self, valore):
        """Cerca un nodo nell'albero."""
        return self._cerca(self.radice, valore)

    def _cerca(self, corrente, valore):
        """Metodo interno ricorsivo di ricerca."""
        if corrente is None:
            return None
        if valore == corrente.etichetta:
            return corrente
        elif valore < corrente.etichetta:
            return self._cerca(corrente.nodo_sinistro, valore)
        else:
            return self._cerca(corrente.nodo_destro, valore)

    def stampa_in_ordine(self, nodo=None):
        """Stampa i valori dell'albero in ordine crescente."""
        if nodo is None:
            nodo = self.radice
        if nodo is None:
            return  # Albero vuoto, niente da stampare
        # VISITA IN ORDINE: sinistro -> corrente -> destro
        if nodo.nodo_sinistro:
            self.stampa_in_ordine(nodo.nodo_sinistro)
        print(nodo.etichetta, end=" ")
        if nodo.nodo_destro:
            self.stampa_in_ordine(nodo.nodo_destro)

    def cancella_nodo(self, valore):
        """Cancella un nodo dato il valore."""
        self.radice = self._cancella(self.radice, valore)

    def _cancella(self, corrente, valore):
        """Metodo interno ricorsivo per cancellare un nodo."""
        if corrente is None:
            return corrente

        if valore < corrente.etichetta:
            corrente.nodo_sinistro = self._cancella(corrente.nodo_sinistro, valore)
        elif valore > corrente.etichetta:
            corrente.nodo_destro = self._cancella(corrente.nodo_destro, valore)
        else:
            # Caso 1: nodo senza figli
            if corrente.nodo_sinistro is None and corrente.nodo_destro is None:
                return None
            # Caso 2: nodo con un solo figlio
            if corrente.nodo_sinistro is None:
                return corrente.nodo_destro
            elif corrente.nodo_destro is None:
                return corrente.nodo_sinistro
            # Caso 3: nodo con due figli
            successore = self._minimo(corrente.nodo_destro)
            corrente.etichetta = successore.etichetta
            corrente.nodo_destro = self._cancella(corrente.nodo_destro, successore.etichetta)

        return corrente

    def _minimo(self, nodo):
        """Trova il nodo con il valore minimo (più a sinistra)"""
        corrente = nodo
        while corrente.nodo_sinistro:
            corrente = corrente.nodo_sinistro
        return corrente

    def _massimo(self, nodo):
        """Trova il nodo con il valore massimo (più a destra)"""
        corrente = nodo
        while corrente.nodo_destro:
            corrente = corrente.nodo_destro
        return corrente