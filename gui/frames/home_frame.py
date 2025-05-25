from tkinter import ttk
from gui.menu import scelte

class HomeFrame(ttk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller  # Salva il riferimento

        ttk.Label(self, text="Benvenuto in Autobus", font=("Arial", 24)).pack(pady=20)
        ttk.Label(self, text="UNIPA: Gruppo di Algoritmi 24 25 ", font=("Arial", 15)).pack()

        ttk.Label(self, text="Apri un file dal menu o scegli una struttura dati qui sotto", font=("Arial", 9)).pack()

        for sezione in scelte:
            label_frame = ttk.LabelFrame(self, text=sezione["nome"], padding=10)
            label_frame.pack(fill='x', padx=20, pady=10)

            for possibile in sezione["possibili"]:
                riga = ttk.Frame(label_frame)
                riga.pack(fill='x', padx=10, pady=5)

                label = ttk.Label(riga, text=possibile["nome"], font=("Arial", 12), anchor="w")
                label.pack(side="left", fill="x", expand=True)

                bottone = ttk.Button(
                    riga,
                    text=possibile["btn_text"],
                    command=lambda op=possibile["btn_action"]: self.controller.dispatch(op)
                )

                bottone.pack(side="right")


        ttk.Label(self, text="Nomi", font=("Arial", 9), anchor="w").pack()