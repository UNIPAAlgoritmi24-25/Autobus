from tkinter import ttk
import tkinter as tk
import Coda as stru  # Importa la classe Coda dal modulo coda.py

class Coda(ttk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        ttk.Label(self, text="Coda", font=("Arial", 24)).pack(pady=20)

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

        self.coda = stru.Coda()  # Istanza della struttura dati Coda

        self.queue_frame = ttk.Frame(self)
        self.queue_frame.pack(pady=10)

        self.aggiorna_coda()

    def aggiorna_coda(self):
        for widget in self.queue_frame.winfo_children():
            widget.destroy()

        corrente = self.coda.inizio
        i = 0
        while corrente is not None:
            nodo = ttk.Button(self.queue_frame, text=f"{corrente.valore}", width=15)
            nodo.grid(row=0, column=i, padx=5, pady=2)
            corrente = corrente.successore
            i += 1

    def aggiungi_valore(self):
        valore = self.aggiungi_inp.get()
        if valore:
            self.coda.aggiungi(valore)
            self.aggiungi_inp.delete(0, tk.END)
            self.aggiorna_coda()

    def rimuovi_valore(self):
        self.coda.rimuovi()
        self.aggiorna_coda()

    def controlla_vuota(self):
        vuota = self.coda.coda_vuota()
        self.label_vuota.config(text="Sì" if vuota else "No")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("GUI Coda")
    coda_gui = CodaGUI(root)
    coda_gui.pack(fill="both", expand=True)
    root.mainloop()
