import tkinter as tk
from tkinter import ttk, filedialog
#equazione di ricorrenza e pseudocodice per lo scritto
from gui.frames.home_frame import HomeFrame
from gui.frames.sort.Counting import Counting
from gui.frames.sort.Marge import Marge
from gui.frames.sort.Bubble import Bubble
from gui.frames.sort.Quik import Quik
from gui.frames.sort.Insertion import Insertion
from gui.frames.scelta_frame import SceltaFrame
from gui.frames.apri_file_frame import ApriFile
from gui.frames.sort.compara import Compara
from gui.frames.pila import Pila



class MainApp(tk.Tk):
    def dispatch(self, action):
        frame = [Counting, Marge, Bubble, Insertion, Quik, Compara, Pila]

        self.show_frame(frame[action])

    def __init__(self):
        super().__init__()
        self.title("Autobus")
        self.geometry("1800x600")
        self.create_menu()

        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.show_frame(HomeFrame)

    def create_menu(self):
        menu_bar = tk.Menu(self)

        # Menu "Home"
        home_menu = tk.Menu(menu_bar, tearoff=0)
        home_menu.add_command(label="Home Page", command=self.open_home)
        home_menu.add_separator()
        home_menu.add_command(label="Esci", command=self.quit)
        menu_bar.add_cascade(label="Home", menu=home_menu)

        # Menu "File"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Apri", command=self.open_file)
        file_menu.add_command(label="Apri", command=self.ApriFile)

        menu_bar.add_cascade(label="File", menu=file_menu)

        # Menu "Ordinamento"
        sort_menu = tk.Menu(menu_bar, tearoff=0)
        sort_menu.add_command(label="Counting Sort", command=lambda: self.dispatch(0))
        sort_menu.add_command(label="Merge Sort", command=lambda: self.dispatch(1))
        sort_menu.add_command(label="Bubble Sort", command=lambda: self.dispatch(2))
        sort_menu.add_command(label="Insertion Sort", command=lambda: self.dispatch(3))
        sort_menu.add_command(label="Quick Sort", command=lambda: self.dispatch(4))
        sort_menu.add_separator()
        sort_menu.add_command(label="Compara", command=lambda: self.dispatch(5))
        menu_bar.add_cascade(label="Ordinamento", menu=sort_menu)

        # Menu "Strutture Dati Lineari"
        linear_menu = tk.Menu(menu_bar, tearoff=0)
        linear_menu.add_command(label="Pila", command=lambda: self.dispatch(6))
        linear_menu.add_command(label="Coda", command=self.open_home)
        linear_menu.add_command(label="Liste", command=self.open_home)
        menu_bar.add_cascade(label="Lineari", menu=linear_menu)

        # Menu "Strutture Dati non Lineari"
        non_linear_menu = tk.Menu(menu_bar, tearoff=0)
        non_linear_menu.add_command(label="Grafi", command=self.open_home)
        non_linear_menu.add_command(label="Alberi", command=self.open_home)
        menu_bar.add_cascade(label="Non Lineari", menu=non_linear_menu)

        self.config(menu=menu_bar)

    def show_frame(self, frame_class):
        for widget in self.container.winfo_children():
            widget.destroy()
        frame = frame_class(self.container, self)
        frame.pack(fill="both", expand=True)

    def open_home(self):
        self.show_frame(HomeFrame)

    def open_home(self):
        self.show_frame(HomeFrame)

    def open_file(self):
        self.show_frame(SceltaFrame)

    def ApriFile(self):
        self.show_frame(ApriFile)
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
