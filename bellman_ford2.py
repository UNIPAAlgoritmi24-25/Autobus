def bellman_ford(grafo, sorgente):
    # Inizializza le distanze
    distanza = {nodo: float("inf") for nodo in grafo.nodi}
    distanza[sorgente] = 0

    # Rilassa gli archi ripetutamente
    for _ in range(len(grafo.nodi) - 1):
        for arco in grafo.archi:
            u = arco.partenza
            v = arco.destinazione
            if distanza[u] + arco.peso < distanza[v]:
                distanza[v] = distanza[u] + arco.peso

    # Controlla cicli negativi
    for arco in grafo.archi:
        u = arco.partenza
        v = arco.destinazione
        if distanza[u] + arco.peso < distanza[v]:
            raise ValueError("Il grafo contiene un ciclo negativo")

    return distanza