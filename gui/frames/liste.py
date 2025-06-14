from tkinter import ttk
import tkinter as tk
import Liste as stru  # Importa la classe Coda dal modulo coda.py

class Lista(ttk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)


        ttk.Label(self, text="Liste connesse", font=("Arial", 24)).pack(pady=20)

        self.table_frame = ttk.Frame(self)
        self.table_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Configuro le colonne per allargarsi
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.columnconfigure(1, weight=1)
        self.table_frame.columnconfigure(2, weight=1)

        # Creo i frame
        self.frameLC =  ttk.Frame(self.table_frame, relief="ridge", borderwidth=2)
        self.frameLD = ttk.Frame(self.table_frame, relief="ridge", borderwidth=2)
        self.frameLN = ttk.Frame(self.table_frame, relief="ridge", borderwidth=2)
        i = 0
        # Li metto nel grid
        self.frameLC.grid(row=i, column=0, sticky="NSEW", padx=5, pady=5)
        self.frameLD.grid(row=i, column=1, sticky="NSEW", padx=5, pady=5)
        self.frameLN.grid(row=i, column=2, sticky="NSEW", padx=5, pady=5)


        self.LC = stru.Lista(True, False)
        self.LD = stru.Lista(False, True)
        self.LN = stru.Lista()

        # Puntatori correnti
        self.LC.pun = None
        self.LD.pun = None
        self.LN.pun = None

        # Etichette dentro i frame
        ttk.Label(self.frameLC, text="Lista connessa Circolare", font=("Arial", 10)).grid(pady=20, row=i, column=0)
        ttk.Label(self.frameLD, text="Lista connessa Doppia", font=("Arial", 10)).grid(pady=20, row=i, column=0)
        ttk.Label(self.frameLN, text="Lista connessa Normale", font=("Arial", 10)).grid(pady=20, row=i, column=0,  sticky="NSEW")
        i += 1


        self.E_LC = tk.Entry(self.frameLC)
        self.E_LC.grid(row=i, column=0)

        self.E_LD = tk.Entry(self.frameLD)
        self.E_LD.grid(row=i, column=0)

        self.E_LN = tk.Entry(self.frameLN)
        self.E_LN.grid(row=i, column=0)

        btn = ttk.Button(self.frameLC, text="Aggiungi in testa", command=lambda: self.aggiungi(self.LC,self.E_LC.get(),False))
        btn.grid(row=i, column=1)
        btn = ttk.Button(self.frameLD, text="Aggiungi in testa", command=lambda: self.aggiungi(self.LD,self.E_LD.get(),False))
        btn.grid(row=i, column=1)
        btn = ttk.Button(self.frameLN, text="Aggiungi in testa", command=lambda: self.aggiungi(self.LN,self.E_LN.get(),False))
        btn.grid(row=i, column=1)

        btn = ttk.Button(self.frameLC, text="Aggiungi in coda", command=lambda: self.aggiungi(self.LC,self.E_LC.get(),True))
        btn.grid(row=i, column=2)
        btn = ttk.Button(self.frameLD, text="Aggiungi in coda", command=lambda: self.aggiungi(self.LD,self.E_LD.get(),True))
        btn.grid(row=i, column=2)
        btn = ttk.Button(self.frameLN, text="Aggiungi in coda", command=lambda: self.aggiungi(self.LN,self.E_LN.get(),True))
        btn.grid(row=i, column=2)
        i += 1

        btn = ttk.Button(self.frameLC, text="avanti", command=lambda: self.avanza(self.lab_testa_LC,self.LC))
        btn.grid(row=i, column=2)
        self.lab_testa_LC = ttk.Label(self.frameLC, text="TESTA")
        self.lab_testa_LC.grid(row=i, column=1)
        btn = ttk.Button(self.frameLC, text="indietro", state="disabled")
        btn.grid(row=i, column=0)

        btn = ttk.Button(self.frameLD, text="avanti", command=lambda: self.avanza(self.lab_testa_LD,self.LD))
        btn.grid(row=i, column=2)
        self.lab_testa_LD = ttk.Label(self.frameLD, text="TESTA")
        self.lab_testa_LD.grid(row=i, column=1)
        btn = ttk.Button(self.frameLD, text="indietro", command=lambda:self.indietreggia(self.lab_testa_LD, self.LD))
        btn.grid(row=i, column=0)

        self.lab_testa_LN = ttk.Label(self.frameLN, text="TESTA")
        self.lab_testa_LN.grid(row=i, column=1)

        self.btn_avanti_LN = ttk.Button(self.frameLN, text="avanti",
                                        command=lambda: self.avanza(self.lab_testa_LN, self.LN))
        self.btn_avanti_LN.grid(row=i, column=2)

        self.btn_indietro_LN = ttk.Button(self.frameLN, text="indietro", state="disabled")
        self.btn_indietro_LN.grid(row=i, column=0)
        i += 1

        mmlLC = ttk.Label(self.frameLC, text="Massimo/Minimo")
        mmlLC.grid(row=i, column=2)
        mmlLD = ttk.Label(self.frameLD, text="Massimo/Minimo")
        mmlLD.grid(row=i, column=2)
        mmlLN = ttk.Label(self.frameLN, text="Massimo/Minimo")
        mmlLN.grid(row=i, column=2)

        btn = ttk.Button(self.frameLC, text="Massimo", command=lambda: self.max(self.LC, mmlLC))
        btn.grid(row=i, column=1)

        btn = ttk.Button(self.frameLD, text="Massimo", command=lambda: self.max(self.LD, mmlLD))
        btn.grid(row=i, column=1)


        btn = ttk.Button(self.frameLN, text="Massimo", command=lambda: self.max(self.LN, mmlLN))
        btn.grid(row=i, column=1)


        btn = ttk.Button(self.frameLC, text="Minimo", command=lambda: self.min(self.LC, mmlLC))
        btn.grid(row=i, column=0)
        btn = ttk.Button(self.frameLD, text="Minimo", command=lambda: self.min(self.LD, mmlLD))
        btn.grid(row=i, column=0)
        btn = ttk.Button(self.frameLN, text="Minimo", command=lambda: self.min(self.LN, mmlLN))
        btn.grid(row=i, column=0)
        i += 1
        self.label_stampaframeLC = ttk.Label(self.frameLC, text="...", font=("Arial", 12), foreground="blue",
                                             anchor="center")
        self.label_stampaframeLD = ttk.Label(self.frameLD, text="...", font=("Arial", 12), foreground="blue",
                                             anchor="center")
        self.label_stampaframeLN = ttk.Label(self.frameLN, text="...", font=("Arial", 12), foreground="blue",
                                             anchor="center")

        self.label_stampaframeLC.grid(row=i, column=0, padx=10, pady=5, sticky="EW")
        self.label_stampaframeLD.grid(row=i, column=0, padx=10, pady=5, sticky="EW")
        self.label_stampaframeLN.grid(row=i, column=0, padx=10, pady=5, sticky="EW")

    def stampa_lista(self, lista):
        output = []
        corrente = lista.indice.successore
        while corrente and corrente != lista.indice:
            output.append(str(corrente.valore))
            corrente = corrente.successore
        return "\n↓\n ".join(output) + "\n↓\nØ"

    def aggiungi(self, lista, valore, incoda):

        if incoda:
            lista.aggiungi_in_coda(valore)
        else:
            lista.aggiungi(valore)
        lista.pun = lista.indice
        self.aggiorna()

    def aggiorna(self):
        lab_LC = self.stampa_lista(self.LC)
        lab_LD = self.stampa_lista(self.LD)
        lab_LN = self.stampa_lista(self.LN)
        self.label_stampaframeLC.config(text=lab_LC)
        self.label_stampaframeLD.config(text=lab_LD)
        self.label_stampaframeLN.config(text=lab_LN)

        # Ripristino i puntatori correnti a inizio lista
        self.corrente_LC = self.LC.indice
        self.corrente_LD = self.LD.indice
        self.corrente_LN = self.LN.indice




    def avanza(self, label, lista):
        if lista.pun and lista.pun.successore:
            lista.pun = lista.pun.successore
            label.config(text=lista.pun.valore)
        else:
            label.config(text="NO SUCCESSORE")

    def indietreggia(self, label,lista):
        if lista.pun and lista.pun.precedente:
            lista.pun = lista.pun.precedente
            label.config(text=lista.pun.valore)
        else:
            label.config(text="NO PRECEDENTE")

    def max(self,lista,label):
        x = lista.get_max()
        label.config(text=x)

    def min(self,lista,label):
        x = lista.get_min()
        print(x)
        label.config(text=x)