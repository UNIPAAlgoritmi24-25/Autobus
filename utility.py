def stampa_matrice_2x2(matrice):
    n = len(matrice)
    m = len(matrice[0])
    print(f"Matrice {n} x {m}:")
    count = ""
    for i in range(m):
        count += f"{i+1}\t"
    print(f"\033[31m\t\t {count} \n\033[0m")
    rign = 0
    for i in matrice:
        rign +=1
        rig = f"\033[34m{rign} \t\t \033[0m"
        for cella in i:
            rig += f"{cella}\t"
        print(rig)