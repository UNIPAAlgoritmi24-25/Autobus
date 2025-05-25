from tkinter import ttk
import tkinter as tk
import Grafo as stu  # Questo è il modulo dove hai definito la classe Pila con Nodo

class Grafo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Grafo", font=("Arial", 24)).pack(pady=20)
