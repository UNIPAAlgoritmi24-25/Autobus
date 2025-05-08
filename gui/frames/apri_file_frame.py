from tkinter import ttk
from gui.widgets.table import Table

class ApriFile(ttk.Frame):
    def __init__(self, parent, controller, headers=None, data=None):
        super().__init__(parent)
        ttk.Label(self, text="Contenuto del file", font=("Arial", 24)).pack(pady=20)

        table_frame = ttk.Frame(self)
        table_frame.pack()

        if headers and data:
            self.table = Table(table_frame, headers, data)
        else:
            ttk.Label(self, text="Nessun dato disponibile.").pack()
