import Coda
import Liste
import itertools
import heapq
from enum import Enum

class COLORE(Enum):
    BIANCO = 1
    GRIGIO = 0
    NERO = -1

class Nodo:
    def __init__(self, etichetta):
        self.etichetta = etichetta
        self.colore = COLORE.BIANCO
    def __str__(self):
        return f"Nodo_{self.etichetta}"

class Arco:
    def __init__(self, partenza, destinazione, peso = 0):
        self.peso = peso
        self.partenza = partenza
        self.destinazione = destinazione

    def __str__(self):
        return f"Arco: Da:{self.partenza}, A:{self.destinazione}, Peso: {self.peso}"
    def edge(self):
        return [self.partenza, self.destinazione]

class Grafo:
    def __init__(self, nodi=None, archi=None, nome = "Nuovo Grafo"):
        self.nome = nome
        self.nodi = nodi if nodi is not None else []
        self.archi = archi if archi is not None else []

    def nullo(self):
        return not len(self.archi) > 0

    def adiacenza_m(self):
        matrice = [[0] * len(self.nodi) for _ in range(len(self.nodi))]

        for arco in self.archi:
            i = self.nodi.index(arco.partenza)
            j = self.nodi.index(arco.destinazione)

            matrice[i][j] = arco.peso  # Solo da partenza a destinazione


        return matrice

    def grado(self, nodo):
        i = 0
        for arco in self.archi:
            if nodo in arco.edge():
                i+=1
        return i

    def gradi(self):
        gradi = []
        for nodo in self.nodi:
            gradi.append(self.grado(nodo))
        return gradi

    def grado_massimo(self):
        return max(self.gradi())

    def grado_minimo(self):
        return min(self.gradi())


    def adiacenza_l(self):
        adiacenza = [Liste.Lista(False, False) for _ in range(len(self.nodi))]

        for i in range(len(adiacenza)):
            nodo_corrente = self.nodi[i]
            adiacenza[i].aggiungi_in_coda("|" + str(nodo_corrente) + "|")

            for arco in self.archi:
                if arco.partenza == nodo_corrente:
                    # Aggiungi sempre la destinazione
                    adiacenza[i].aggiungi_in_coda(arco.destinazione.etichetta)

        return adiacenza

    def densita(self):
        n = len(self.nodi)
        e = len(self.archi)
        return (2 * e)/(n*(n-1))
    def indicenza(self):
        matrice = []
        for nodo in self.nodi:
            riga = []
            for arco in self.archi:
                if arco.partenza == nodo:
                    riga.append(1)
                elif arco.destinazione == nodo:
                    riga.append(-1)
                else:
                    riga.append(0)

            matrice.append(riga)
        return matrice

    def descrivi(self):
        x = f"Nome Grafo: {self.nome} \n"
        x += f"Archi ({len(self.archi)}) : \n"
        for arco in self.archi:
            x += f"\t{arco} \n"

        x += f"Nodi ({len(self.nodi)}) : \n"
        for nodo in self.nodi:
            x += f"\t{nodo} \n"
        return x

    def visita_BFS(self, indice):
        if indice > len(self.nodi) - 1:
            print("Indice Sorgente Errato")
            return None
        else:
            sorgente = self.nodi[indice-1]
            output = []

        for nodo in self.nodi:
            nodo.colore = COLORE.BIANCO

        sorgente.colore = COLORE.GRIGIO
        coda = Coda.Coda()
        coda.aggiungi(sorgente)

        while not coda.coda_vuota():
            u = coda.rimuovi()
            output.append(u)
            # Itera sugli archi che partono da u
            for arco in self.archi:
                if arco.partenza == u and arco.destinazione.colore == COLORE.BIANCO:
                    v = arco.destinazione
                    v.colore = COLORE.GRIGIO
                    coda.aggiungi(v)

            u.colore = COLORE.NERO

        return output

    def prim(self, sorgente):
        visitati = set()
        mst_archi = []
        heap = []

        visitati.add(sorgente)

        # Aggiungi tutti gli archi in uscita dal nodo sorgente
        for arco in self.archi:
            if arco.partenza == sorgente:
                heapq.heappush(heap, (arco.peso, arco))

        while heap and len(visitati) < len(self.nodi):
            peso, arco = heapq.heappop(heap)

            if arco.destinazione in visitati:
                continue

            mst_archi.append(arco)
            visitati.add(arco.destinazione)

            # Aggiungi nuovi archi in uscita dal nodo appena aggiunto
            for prossimo in self.archi:
                if prossimo.partenza == arco.destinazione and prossimo.destinazione not in visitati:
                    heapq.heappush(heap, (prossimo.peso, prossimo))

        return mst_archi

    def dijkstra(self, sorgente):
        distanze = {n: float('inf') for n in self.nodi}
        precedente = {n: None for n in self.nodi}
        distanze[sorgente] = 0
        contatore = itertools.count()
        heap = [(0, next(contatore), sorgente)]

        while heap:
            distanza_u, _, u = heapq.heappop(heap)
            for arco in self.archi:
                if arco.partenza == u:
                    v = arco.destinazione
                    peso = arco.peso
                    if distanze[u] + peso < distanze[v]:
                        distanze[v] = distanze[u] + peso
                        precedente[v] = u
                        heapq.heappush(heap, (distanze[v], next(contatore), v))

        return distanze, precedente


    def ricostruisci_cammino(self, precedente, destinazione):
        cammino = []
        while destinazione:
            cammino.insert(0, destinazione)
            destinazione = precedente[destinazione]
        return cammino





