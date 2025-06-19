import Grafi as stu


nodi = [stu.Nodo(str(i)) for i in range(1,6)]
archi = [
    stu.Arco(nodi[0], nodi[1], 1),
    stu.Arco(nodi[0], nodi[4], 10),
    stu.Arco(nodi[1], nodi[4], 15),
    stu.Arco(nodi[4], nodi[3], 3),
    stu.Arco(nodi[1], nodi[3], 20),
    stu.Arco(nodi[1], nodi[2], 16),
    stu.Arco(nodi[3], nodi[2], 150)
]
g = stu.Grafo(nodi, archi)

print(g.densita())

# Poi cambia archi o nodi e crea un nuovo grafo:
nodi2 = [stu.Nodo(str(i)) for i in range(1,4)]
archi2 = [stu.Arco(nodi2[0], nodi2[1], 2), stu.Arco(nodi2[1], nodi2[2], 5)]
g2 = stu.Grafo(nodi2, archi2)
print(g2.densita())
