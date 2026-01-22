import customtkinter as ctk
from py.backend import notas
import op2_search as search

nomes, salas, materias, aluno_sala = notas.load_names()

class AutocompleteEntry(ctk.CTkEntry):
    def __init__(self, parent, placeholder_text="", values=None, *args, **kwargs):
        super().__init__(parent, placeholder_text=placeholder_text, *args, **kwargs)
        self.values = values if values is not None else []
        self.optionmenu = ctk.CTkOptionMenu(parent, values=[])
        self.optionmenu.set(" ")
        self.optionmenu.grid(row=self.grid_info()["row"] + 1, column=self.grid_info()["column"], sticky="ew", padx=5)
        self.bind("<KeyRelease>", self.on_keyrelease)
        self.optionmenu.bind("<<CTkOptionMenuSelected>>", self.select_item)

    def on_keyrelease(self, event):
        typed = self.get().lower()
        if typed == "":
            self.optionmenu.configure(values=[])
            return

        filtered = [value for value in self.values if typed in value.lower()]
        self.optionmenu.configure(values=filtered)

    def select_item(self, event):
        selected = self.optionmenu.get()
        self.delete(0, ctk.END)
        self.insert(0, selected)
        self.optionmenu.configure(values=[])