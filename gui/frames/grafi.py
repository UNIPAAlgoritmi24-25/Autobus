from tkinter import ttk
from gui.widgets.table import Table
from tkinter import filedialog, messagebox
import Grafi as stu  # Questo è il modulo dove hai definito la classe Pila con Nodo





class Grafo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        super().__init__(parent)
        self.rowconfigure(0, weight=0)   # riga scritta (non espande)
        self.rowconfigure(1, weight=1)   # riga dei frame (espande)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.controller = controller

        n1 = stu.Nodo("1")
        n2 = stu.Nodo("2")
        n3 = stu.Nodo("3")
        n4 = stu.Nodo("4")
        n5 = stu.Nodo("5")
        a1 = stu.Arco(n1, n2, 1)
        a2 = stu.Arco(n1, n5, 10)
        a3 = stu.Arco(n2, n5, 15)
        a4 = stu.Arco(n5, n4, 3)
        a5 = stu.Arco(n2, n4, 20)
        a6 = stu.Arco(n2, n3, 16)
        a7 = stu.Arco(n4, n3, 150)
        self.gra = stu.Grafo([n1, n2, n3, n4, n5], [a1, a2, a3, a4, a5, a6, a7])

        label = ttk.Label(self, text="Grafo", font=("Arial", 24))
        label.grid(row=0, column=0, padx=10, pady=5, sticky="n", columnspan=2)


        self.comandi = ttk.Frame(self)
        self.comandi.grid(row=1, column=0, sticky="nsew")
        self.risultati = ttk.Frame(self)
        self.risultati.grid(row=1, column=1, sticky="nsew")
        self.label_stampa = ttk.Label(self.risultati, text="Qui vedrai la stuttura", font=("Arial", 12), foreground="blue")
        self.label_risultato = ttk.Label(self.risultati, text="", font=("Arial", 14))
        self.label_stampa.grid(row=0, column=0, padx=10, pady=5)
        self.label_risultato.grid(row=1, column=0, padx=10, pady=5)


        i=0
        # Campo per inserire valore da cercare
        self.label = ttk.Label(self.comandi,text="Inserisci valore da cercare")
        self.label.grid(row=i, column=0, padx=10, pady=5)
        self.entry_valore = ttk.Entry(self.comandi)
        self.entry_valore.grid(row=i, column=1, padx=10, pady=5)
        btn_cerca = ttk.Button(self.comandi, text="Cerca", command=self.cerca_valore)
        btn_cerca.grid(row=i, column=2, padx=10, pady=5)

        i+=1
        # Campo per inserire valore da cercare
        label = ttk.Label(self.comandi,text="Grado")
        self.grado_valore = ttk.Entry(self.comandi)
        grado_btn = ttk.Button(self.comandi, text="Calcola Grado", command=self.grado)
        grado_btn_min = ttk.Button(self.comandi, text="min", command=self.grado_min)
        grado_btn_max = ttk.Button(self.comandi, text="max", command=self.grado_max)

        grado_btn.grid(row=i, column=2, padx=10, pady=5)
        label.grid(row=i, column=0, padx=10, pady=5)
        self.grado_valore.grid(row=i, column=1, padx=10, pady=5)
        grado_btn_min.grid(row=i, column=4, padx=10, pady=5)
        grado_btn_max.grid(row=i, column=3, padx=10, pady=5)

        i += 1
        # Campo per inserire valore da cercare
        label = ttk.Label(self.comandi,text="Rapresentare il Grafo: ")
        btn_in_mat = ttk.Button(self.comandi, text="Indicenza", command=self.rapresenta_in_mat)
        btn_in_arr = ttk.Button(self.comandi, text="Addiacienza - Lista", command=self.rapresenta_in_arr)
        btn_ic_mat = ttk.Button(self.comandi, text="Addiacienza - Matrice", command=self.rapresenta_ic_mat)
        label.grid(row=i, column=0, padx=10, pady=5)
        btn_in_mat.grid(row=i, column=1, padx=10, pady=5)
        btn_in_arr.grid(row=i, column=2, padx=10, pady=5)
        btn_ic_mat.grid(row=i, column=3, padx=10, pady=5)

        i += 1
        label = ttk.Label(self.comandi, text="Algoritmi:")
        self.entry_algortmi = ttk.Entry(self.comandi)
        btn_prim = ttk.Button(self.comandi, text="Prim", command=self.prim)
        btn_dijkstra = ttk.Button(self.comandi, text="Dijkstra", command=self.dijkstra)
        btn_visita_bfs = ttk.Button(self.comandi, text="Visiita BFS", command=self.bfs)

        self.entry_algortmi.grid(row=i, column=1, padx=10, pady=5)
        label.grid(row=i, column=0, padx=10, pady=5)
        btn_prim.grid(row=i, column=4, padx=10, pady=5)
        btn_dijkstra.grid(row=i, column=2, padx=10, pady=5)
        btn_visita_bfs.grid(row=i, column=3, padx=10, pady=5)

    def rapresenta_in_mat(self):
        self.label_stampa.config(text="Incidenza")
        # Pulisce vecchia tabella (se presente)
        for widget in self.label_risultato.winfo_children():
            widget.destroy()

        # Mostra nuova tabella
        headers = []
        mat =  self.gra.indicenza()
        Table(self.label_risultato, headers,mat)


    def rapresenta_in_arr(self):
        self.label_stampa.config(text="adiacenza per lista - Controlla la console")
        self.label_risultato.config(text="Controlla la console, Grazie")
        for b in (self.gra.adiacenza_l()):
            b.scansiona()


    def rapresenta_ic_mat(self):
        self.label_stampa.config(text="Addiacienza per matrice")
        # Pulisce vecchia tabella (se presente)
        for widget in self.label_risultato.winfo_children():
            widget.destroy()

        # Mostra nuova tabella
        headers = []
        mat = self.gra.adiacenza_m()
        Table(self.label_risultato, headers, mat)


    def cerca_valore(self):
        x = self.cerca_nodo(self.entry_valore.get())
        if x is False:
            self.label_stampa.config(text="Non Esiste")
        else:
            self.label_stampa.config(text=f"Nodo con valore cervato: {x}")


    def bfs(self):
        x = self.cerca_nodo(self.entry_algortmi.get())
        if x is False:
            self.label_stampa.config(text="Non Esiste")
        else:
            y = ""
            for nodo in self.gra.visita_BFS(self.gra.nodi.index(x)):
                y += f"{str(nodo)}, "

            self.label_stampa.config(text=f"{y}")

    def prim(self):
        x = self.cerca_nodo(self.entry_algortmi.get())
        if x is False:
            self.label_stampa.config(text="Non Esiste")
        else:
            y = ""
            for nodo in self.gra.prim(x):
                y += f"{str(nodo)}, \n"

            self.label_stampa.config(text=f"{y}")

    def dijkstra(self):
        x = self.cerca_nodo(self.entry_algortmi.get())
        if x is False:
            self.label_stampa.config(text="Nodo inesistente")
        else:
            risultato = ""
            distanze, precedente = self.gra.dijkstra(x)
            for nodo in self.gra.nodi:
                risultato += f"Distanza da {x} a {nodo}: {distanze[nodo]}\n"
                percorso = self.gra.ricostruisci_cammino(precedente, nodo)
                risultato += "Percorso: " + " -> ".join(str(n) for n in percorso) + "\n\n"

            self.label_stampa.config(text=risultato)

    def grado_min(self):
        self.label_stampa.config(text=f"grado min pari ha {self.gra.grado_minimo()}")

    def grado_max(self):
        self.label_stampa.config(text=f"grado max pari ha {self.gra.grado_massimo()}")

    def grado(self):
        x = self.cerca_nodo(self.grado_valore.get())
        if x is False:
            self.label_stampa.config(text="Non Esiste")
        else:
            print(self.gra.grado(x))
            print(self.gra)
            print(x)
            self.label_stampa.config(text=f"{x} ha grado pari ha {self.gra.grado(x)}")

    def cerca_nodo(self, r):
        for nodo in self.gra.nodi:
            if nodo.etichetta == r:
                return nodo
        return False

    def leggi_file(self):
        percorso_file = filedialog.askopenfilename(
            title="Seleziona un file",
            filetypes=(("File di testo", "*.txt"), ("Tutti i file", "*.*"))
        )
        if percorso_file:
            try:
                with open(percorso_file, "r", encoding="utf-8") as file:
                    contenuto = file.read()

                    messagebox.showinfo("Successo", f"Inseriti {len(contenuto)} nodi nell'albero.")

            except Exception as e:
                messagebox.showerror("Errore", f"Errore durante la lettura: {e}")

