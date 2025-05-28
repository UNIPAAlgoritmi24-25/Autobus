from tkinter import ttk
import tkinter as tk
from tkinter import filedialog, messagebox
import Grafo as stu  # Questo è il modulo dove hai definito la classe Pila con Nodo

class Grafo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Grafo", font=("Arial", 24)).pack(pady=20)

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

