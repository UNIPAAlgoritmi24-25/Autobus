from tkinter import ttk
from gui.menu import tipi

class SceltaFrame(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        ttk.Label(self, text="Scegli il tipo di file", font=("Arial", 24)).pack(pady=20)

        for valore in tipi:
            riga = ttk.Frame(self)
            riga.pack(fill='x', padx=20, pady=10)

            label = ttk.Label(riga, text=valore["nome"], font=("Arial", 12), anchor="center")
            label.grid(row=0, column=0, sticky='ew')  # allineata a sinistra
            riga.columnconfigure(1, weight=1)  # espande la colonna per riempire lo spazio

            label = ttk.Label(riga, text=valore["desc"], font=("Arial", 9), anchor="center")
            label.grid(row=0, column=1, sticky="ew")  # permette al testo di centrarsi
            riga.columnconfigure(1, weight=1)  # espande la colonna per riempire lo spazio

            bottone = ttk.Button(riga, text="Scegli",  command=lambda op=valore["btn_action"]: self.controller.dispatch(op))
            bottone.grid(row=0, column=2, sticky='ew')  # allineato a destra

            # Espande la colonna 0 per "spingere" il bottone a destra
            riga.columnconfigure(0, weight=1)
