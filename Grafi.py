import Coda
import utility
import Liste
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
    def __init__(self, partenza, destinazione, peso = 0, senso_unico = False):
        self.peso = peso
        self.partenza = partenza
        self.destinazione = destinazione
        self.senso_unico = senso_unico

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
        return not len(self.nodi) > 0

    def adiacenza_m(self):
        matrice = [[0] * len(self.nodi) for _ in range(len(self.nodi))]

        for arco in self.archi:
            i = self.nodi.index(arco.partenza)
            j = self.nodi.index(arco.destinazione)

            if arco.senso_unico:
                matrice[i][j] = arco.peso  # Solo da partenza a destinazione
            else:
                matrice[i][j] = arco.peso
                matrice[j][i] = arco.peso  # Anche direzione opposta

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
                elif not arco.senso_unico and arco.destinazione == nodo_corrente:
                    # Se l’arco NON è orientato, aggiungi anche la partenza
                    adiacenza[i].aggiungi_in_coda(arco.partenza.etichetta)

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
                if arco.senso_unico:
                    if arco.partenza == nodo:
                        riga.append(1)
                    elif arco.destinazione == nodo:
                        riga.append(-1)
                    else:
                        riga.append(0)
                else:
                    if nodo == arco.partenza or nodo == arco.destinazione:
                        riga.append(1)
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
        
    def dijkstra(self, sorgente):
        distanze = {n: float('inf') for n in self.nodi}
        precedente = {n: None for n in self.nodi}
        distanze[sorgente] = 0
        heap = [(0, sorgente)]

        while heap:
            distanza_u, u = heapq.heappop(heap)
            for arco in self.archi:
                if arco.partenza == u:
                    v = arco.destinazione
                    peso = arco.peso
                    if distanze[u] + peso < distanze[v]:
                        distanze[v] = distanze[u] + peso
                        precedente[v] = u
                        heapq.heappush(heap, (distanze[v], v))

        return distanze, precedente

    def ricostruisci_cammino(self, precedente, destinazione):
        cammino = []
        while destinazione:
            cammino.insert(0, destinazione)
            destinazione = precedente[destinazione]
        return cammino

# Esempio di utilizzo:
# distanze, precedente = gra.dijkstra(n1)
# for nodo in gra.nodi:
#     print(f"Distanza da {n1} a {nodo}: {distanze[nodo]}")
#     percorso = gra.ricostruisci_cammino(precedente, nodo)
#     print("Percorso:", " -> ".join(str(n) for n in percorso))



n1 = Nodo("1")
n2 = Nodo("2")
n3 = Nodo("3")
n4 = Nodo("4")
n5 = Nodo("5")
a1 = Arco(n1, n2, 1)
a2 = Arco(n1, n5, 1)
a3 = Arco(n2, n5, 1, True)
a4 = Arco(n5, n4, 1)
a5 = Arco(n2, n4, 1)
a6 = Arco(n2, n3, 1)
a7 = Arco(n4, n3, 1)



gra = Grafo([n1, n2, n3, n4, n5], [a1, a2, a3, a4, a5, a6, a7])
print("Grado di n3:")
print(gra.grado(n3))

print("Grado Massimo:")
print(gra.grado_massimo())


print("Grado Minimo:")
print(gra.grado_minimo())

print(gra.descrivi())

print("Grafo nullo")
print(gra.nullo())

print("adiacenza_m")
utility.stampa_matrice_2x2(gra.adiacenza_m())

print("adiacenza_l")
for b in (gra.adiacenza_l()):
    b.scansiona()

print("Indicenza")
utility.stampa_matrice_2x2(gra.indicenza())


print("visita_BFS")
for nodo in gra.visita_BFS(1):
    print(nodo)

