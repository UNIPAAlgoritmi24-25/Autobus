from tkinter import ttk
import tkinter as tk
import Pila as stu  # Questo è il modulo dove hai definito la classe Pila con Nodo

class Pila(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Pila", font=("Arial", 24)).pack(pady=20)

        self.table_frame = ttk.Frame(self)
        self.table_frame.pack()

        self.aggiungi_inp = ttk.Entry(self.table_frame)
        aggiungi = ttk.Button(self.table_frame, text="Aggiungi", width=15, command=self.aggiungi_valore)
        rimuovi = ttk.Button(self.table_frame, text="Rimuovi", width=15, command=self.rimuovi_valore)
        vuota = ttk.Button(self.table_frame, text="È vuota?", width=15, command=self.controlla_vuota)

        aggiungi.grid(row=0, column=0, padx=5, pady=5)
        self.aggiungi_inp.grid(row=0, column=1, padx=5, pady=5)
        rimuovi.grid(row=1, column=0, padx=5, pady=5)
        vuota.grid(row=2, column=0, padx=5, pady=5)

        self.label_vuota = ttk.Label(self.table_frame, text="")
        self.label_vuota.grid(row=2, column=1)

        self.pila = stu.Pila()

        self.stack_frame = ttk.Frame(self)
        self.stack_frame.pack(pady=10)

        self.aggiorna_stack()

    def aggiorna_stack(self):
        for widget in self.stack_frame.winfo_children():
            widget.destroy()

        corrente = self.pila.indice
        i = 0
        while corrente is not None:
            nodo = ttk.Button(self.stack_frame, text=f"{corrente.valore}", width=15)
            nodo.grid(row=i, column=0, padx=5, pady=2)
            corrente = corrente.successore
            i += 1

    def aggiungi_valore(self):
        valore = self.aggiungi_inp.get()
        if valore:
            self.pila.aggiungi(valore)
            self.aggiungi_inp.delete(0, tk.END)
            self.aggiorna_stack()

    def rimuovi_valore(self):
        self.pila.rimuovi()
        self.aggiorna_stack()

    def controlla_vuota(self):
        vuota = self.pila.pila_vuota()
        self.label_vuota.config(text="Sì" if vuota else "No")
