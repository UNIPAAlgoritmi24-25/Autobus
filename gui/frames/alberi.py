from tkinter import ttk
import tkinter as tk
import Alberi as stu  # Modulo dove hai definito la classe AlberoOrdinato
from tkinter import filedialog, messagebox

class Albero(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.albero = stu.AlberoOrdinato()  # Inizializza albero binario ordinato

        ttk.Label(self, text="Albero Binario", font=("Arial", 24)).pack(pady=20)

        # Bottone per caricare file
        pulsante = tk.Button(self, text="Apri file", command=self.leggi_file)
        pulsante.pack(pady=5)

        # Campo per inserire valore da cercare
        self.entry_valore = ttk.Entry(self)
        self.entry_valore.pack(pady=5)
        self.entry_valore.insert(0, "Inserisci valore da cercare")

        # Bottone per ricerca
        btn_cerca = tk.Button(self, text="Cerca", command=self.cerca_valore)
        btn_cerca.pack(pady=5)

        # Pulsante stampa struttura albero (visiva)
        btn_stampa_struttura = tk.Button(self, text="Stampa struttura albero", command=self.stampa_struttura)
        btn_stampa_struttura.pack(pady=5)

        # Pulsante stampa in ordine (in-order traversal)
        btn_stampa_in_ordine = tk.Button(self, text="Stampa in ordine", command=self.stampa_in_ordine)
        btn_stampa_in_ordine.pack(pady=5)

        # Label per mostrare il risultato
        self.label_risultato = ttk.Label(self, text="", font=("Arial", 14))
        self.label_risultato.pack(pady=10)
        # Label per output stampa in ordine
        self.label_stampa = ttk.Label(self, text="", font=("Arial", 12), foreground="blue")
        self.label_stampa.pack(pady=10)
    def leggi_file(self):
        percorso_file = filedialog.askopenfilename(
            title="Seleziona un file",
            filetypes=(("File di testo", "*.txt"), ("Tutti i file", "*.*"))
        )
        if percorso_file:
            try:
                with open(percorso_file, "r", encoding="utf-8") as file:
                    contenuto = file.read()
                    valori = [int(x) for x in contenuto.replace('\n', ' ').split() if x.strip().isdigit()]
                    for valore in valori:
                        self.albero.aggiungi_nodo(valore)
                    messagebox.showinfo("Successo", f"Inseriti {len(valori)} nodi nell'albero.")
            except Exception as e:
                messagebox.showerror("Errore", f"Errore durante la lettura: {e}")

    def cerca_valore(self):
        valore = self.entry_valore.get()
        if not valore.isdigit():
            self.label_risultato.config(text="Inserisci un numero valido")
            return

        valore = int(valore)
        nodo = self.albero.cerca(valore)
        if nodo:
            self.label_risultato.config(text=f"Trovato: {nodo.etichetta}")
        else:
            self.label_risultato.config(text="Valore non trovato")

    def stampa_struttura(self):
        print("\nStruttura dell'albero:")
        self.albero.stampa()

    def stampa_in_ordine(self):
        # Catturiamo la stampa in ordine in una stringa
        risultati = []

        def visita_in_ordine(nodo):
            if nodo is None:
                return
            visita_in_ordine(nodo.nodo_sinistro)
            risultati.append(str(nodo.etichetta))
            visita_in_ordine(nodo.nodo_destro)

        visita_in_ordine(self.albero.radice)
        testo = " ".join(risultati)
        self.label_stampa.config(text= testo if testo else "Albero vuoto")