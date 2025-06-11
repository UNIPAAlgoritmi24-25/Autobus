import time
from tkinter import ttk
from gui.menu import bubble as desc
from gui.widgets.table import Table
import Ordinamento as ord
class Bubble(ttk.Frame):

    def cancella(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

    def test(self):
        self.cancella()
        self.label_test.config(text="Test in corso")
        dataset = ord.dataset(negativi=False,  taglie=[10,50,100,1000])
        risultati = []

        for test in dataset:
            start_time = time.time()
            ord.bubble_sort(test)
            end_time = time.time()
            execution_time = end_time - start_time
            risultati.append((len(test), f"{execution_time:.6f} s"))
            self.cancella()
            self.label_test.config(text=f"Test in corso: Dataset: {len(test)}, {execution_time:.6f} s")

        # Mostra "Finito"
        self.cancella()
        self.label_test.config(text="Finito")

        # Pulisce vecchia tabella (se presente)


        # Mostra nuova tabella
        headers = ["Dimensione", "Tempo di esecuzione"]
        Table(self.table_frame, headers, risultati)

    def __init__(self, parent, controller=None):
        super().__init__(parent)

        # Etichette iniziali
        ttk.Label(self, text="Bubble Sort", font=("Arial", 24)).pack(pady=20)

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

