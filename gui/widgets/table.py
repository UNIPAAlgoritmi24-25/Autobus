import tkinter as tk

class Table:
    def __init__(self, root, headers, data):
        self.entries = []

        for j, header in enumerate(headers):
            label = tk.Label(root, text=header, font=('Arial', 12, 'bold'), bg="lightgrey")
            label.grid(row=0, column=j, sticky="nsew")

        for i, row in enumerate(data, start=1):
            entry_row = []
            for j, val in enumerate(row):
                e = tk.Entry(root, width=20, fg='blue', font=('Arial', 12))
                e.grid(row=i, column=j, sticky="nsew")
                e.insert(tk.END, val)
                entry_row.append(e)
            self.entries.append(entry_row)
