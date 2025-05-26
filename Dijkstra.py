import heapq

class Grafo:
    def __init__(self, nodi=None, archi=None, nome = "Nuovo Grafo"):
        self.nome = nome
        self.nodi = nodi if nodi is not None else []
        self.archi = archi if archi is not None else []


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
