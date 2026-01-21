# gui/op1_add.py
from py.backend import notas
import customtkinter as ctk

class AddNotaFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.entry_nome = ctk.CTkEntry(self)
        self.entry_nome.pack()
        self.entry_sala = ctk.CTkEntry(self)
        self.entry_sala.pack()
        self.btn_add = ctk.CTkButton(self, text="Adicionar Nota", command=self.adicionar)
        self.btn_add.pack()

    def adicionar(self):
        nome = self.entry_nome.get()
        sala = self.entry_sala.get()
        notas.add_grade(nome, sala, "Matemática", "Prova 1", 9.5)
