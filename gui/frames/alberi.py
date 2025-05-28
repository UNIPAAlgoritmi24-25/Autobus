from tkinter import ttk
import tkinter as tk
import Alberi as stu  # Modulo dove hai definito la classe AlberoOrdinato
from tkinter import filedialog, messagebox

class Albero(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.rowconfigure(0, weight=0)   # riga scritta (non espande)
        self.rowconfigure(1, weight=1)   # riga dei frame (espande)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.controller = controller
        self.albero = stu.AlberoOrdinato()  # Inizializza albero binario ordinato

        label = ttk.Label(self, text="Albero Binario", font=("Arial", 24))
        label.grid(row=0, column=0, padx=10, pady=5, sticky="n", columnspan=2)


        self.comandi = ttk.Frame(self)
        self.comandi.grid(row=1, column=0, sticky="nsew")
        self.risultati = ttk.Frame(self)
        self.risultati.grid(row=1, column=1, sticky="nsew")

        # Bottone per caricare file
        ttk.Label(self.comandi, text="Carica da file").grid(row=1, column=0, padx=10, pady=5)
        pulsante = ttk.Button(self.comandi, text="Apri file", command=self.leggi_file)
        pulsante.grid(row=1, column=1, padx=10, pady=5)



        # Pulsante stampa struttura albero (visiva)
        ttk.Label(self.comandi, text="Stampa struttura albero").grid(row=3, column=0, padx=10, pady=5)
        btn_stampa_struttura = ttk.Button(self.comandi, text="Stampa", command=self.stampa_struttura)
        btn_stampa_struttura.grid(row=3, column=1, padx=10, pady=5)



        # Pulsante stampa in ordine (in-order traversal)

        ttk.Label(self.comandi, text="Stampa  in ordine").grid(row=5, column=0, padx=10, pady=5)
        btn_stampa_in_ordine = ttk.Button(self.comandi, text="Stampa", command=self.stampa_in_ordine)
        btn_stampa_in_ordine.grid(row=5, column=1, padx=10, pady=5)


        ttk.Label(self.comandi, text="Massimo e minimo").grid(row=6, column=0, padx=10, pady=5)
        # Pulsante stampa in ordine (in-order traversal)
        btn_min = ttk.Button(self.comandi, text="Min", command=self.get_min)
        btn_min.grid(row=6, column=1, padx=10, pady=5)

        # Pulsante stampa in ordine (in-order traversal)
        btn_max = ttk.Button(self.comandi, text="Max", command=self.get_max)
        btn_max.grid(row=6, column=2, padx=10, pady=5)

        # Campo per inserire valore da cercare
        self.label = ttk.Label(self.comandi,text="Inserisci valore da cercare")
        self.label.grid(row=8, column=0, padx=10, pady=5)
        self.entry_valore = ttk.Entry(self.comandi)
        self.entry_valore.grid(row=8, column=1, padx=10, pady=5)
        btn_cerca = ttk.Button(self.comandi, text="Cerca", command=self.cerca_valore)
        btn_cerca.grid(row=8, column=3, padx=10, pady=5)

        # Campo per inserire valore da cercare
        self.label_ins = ttk.Label(self.comandi,text="Inserisci valore da Inserire")
        self.label_ins.grid(row=9, column=0, padx=10, pady=5)
        self.ins_valore = ttk.Entry(self.comandi)
        self.ins_valore.grid(row=9, column=1, padx=10, pady=5)
        btn_ins = ttk.Button(self.comandi, text="Ins", command=self.ins_valore_fn)
        btn_ins.grid(row=9, column=3, padx=10, pady=5)

        # Pulsante stampa struttura albero (visiva)
        ttk.Label(self.comandi, text="Elimina un valore").grid(row=10, column=0, padx=10, pady=5)
        btn_stampa_struttura = ttk.Button(self.comandi, text="Elimina", command=self.elimina)
        self.entry_eli = ttk.Entry(self.comandi)
        self.entry_eli.grid(row=10, column=1, padx=10, pady=5)
        btn_stampa_struttura.grid(row=10, column=2, padx=10, pady=5)

        # Label per mostrare il risultato
        self.label_stampa = ttk.Label(self.risultati, text="Qui vedrai la stuttura", font=("Arial", 12), foreground="blue")
        self.label_risultato = ttk.Label(self.risultati, text="", font=("Arial", 14))

        self.label_stampa.grid(row=0, column=0, padx=10, pady=5)
        self.label_risultato.grid(row=1, column=0, padx=10, pady=5)

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
                        self.ins_valore.delete(0, tk.END)  # Cancella il campo
                        self.ins_valore.insert(0, str(valore))  # Inserisce il nuovo valore
                        self.ins_valore_fn()
                    messagebox.showinfo("Successo", f"Inseriti {len(valori)} nodi nell'albero.")
                    self.label_risultato.config(text=f"Inseriti {len(valori)} nodi nell'albero.")
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
    def elimina(self):
        valore = self.entry_eli.get()
        if not valore.isdigit():
            self.label_risultato.config(text="Inserisci un numero valido")
            return

        valore = int(valore)
        nodo = self.albero.cerca(valore)
        if nodo:
            self.albero.cancella_nodo(valore)
            self.label_risultato.config(text=f"Trovato: ed eliminato | NR: {nodo.etichetta}")
        else:
            self.label_risultato.config(text="Valore non trovato")

    def ins_valore_fn(self):
        valore = self.ins_valore.get()
        if not valore.isdigit():
            self.label_risultato.config(text="Inserisci un numero valido")
            return

        valore = int(valore)
        nodo = self.albero.cerca(valore)
        if nodo:
            self.label_risultato.config(text=f"Trovato: esiste gia")
        else:
            self.albero.aggiungi_nodo(valore)
            self.label_risultato.config(text="Valore aggiunto")

    def stampa_struttura(self):
        self.label_stampa.config(text = self.albero.stampa())

    def get_max(self):
        self.label_risultato.config(text = self.albero._massimo(self.albero.radice))

    def get_min (self):
        self.label_risultato.config(text = self.albero._minimo(self.albero.radice))

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
        self.label_risultato.config(text= testo if testo else "Albero vuoto")