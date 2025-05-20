import time
from tkinter import ttk
from gui.menu import Compara as desc
import Ordinamento as ord
import matplotlib.pyplot as plt


class Compara(ttk.Frame):
    def test(self):
        dataset = ord.dataset(negativi=False)
        dati = {}

        for alg in ord.get_alg():
            ris = []
            etichetta = alg["N"]
            for data in dataset:
                start_time = time.time()
                alg["F"](data[:])
                end_time = time.time()
                ris.append((len(data), end_time-start_time))
            dati[etichetta] = ris

        # Traccia ogni linea
        for etichetta, punti in dati.items():
            x = [p[0] for p in punti]
            y = [p[1] for p in punti]
            plt.plot(x, y, label=etichetta)

        # Etichette e legenda
        plt.xlabel('Taglia (N)')  # asse X
        plt.ylabel('Tempo (S)')  # asse Y
        plt.title('Compara ordinamenti')
        plt.legend()
        plt.grid(True)
        plt.show()

    def __init__(self, parent, controller=None):
        super().__init__(parent)

        # Etichette iniziali
        ttk.Label(self, text="Quik Sort", font=("Arial", 24)).pack(pady=20)

        # Creazione della riga
        riga = ttk.Frame(self)
        riga.pack(fill='x', padx=20, pady=10)

        # Colonna 0 - Testo
        x = 0
        for testo in enumerate(desc):
            valore, ogetto = testo[0], testo[1]
            x = valore
            tipo = ogetto["tipo"]
            text = ogetto["testo"]
            font = ("Arial", 10)
            if tipo == 1:
                font = ("Arial", 15)
            ttk.Label(riga, text=text, font=font, wraplength=400).grid(row=valore, column=0, sticky="w")

        ttk.Button(riga, text="Test", command=self.test).grid(row=x + 1, column=0, sticky="we")

        # Colonna 1 - Stato e Tabella
        self.label_test = ttk.Label(riga, text="Inizia il Test", font=("Arial", 25), anchor="center")
        self.label_test.grid(row=0, column=1, sticky="ewns", rowspan=2)

        self.table_frame = ttk.Frame(riga )
        self.table_frame.grid(row=2, column=1, sticky="", pady=10)

        riga.columnconfigure(1, weight=1)


