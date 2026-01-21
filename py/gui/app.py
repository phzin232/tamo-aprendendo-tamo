from py.gui.op1_add import AddNotaFrame
from py.gui.op2_search import SearchAlunoFrame
from py.backend import notas

import customtkinter as ctk

nomes, salas, materias, sala_aluno = notas.load_names()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monitoramento de Notas")
        geometry = "800x600"
        self.geometry(geometry)

        # Botões do menu principal
        self.btn_op1 = ctk.CTkButton(self, text="Adicionar Nota", command=self.mostrar_op1)
        self.btn_op1.pack()

        self.btn_op2 = ctk.CTkButton(self, text="Pesquisar Aluno", command=self.mostrar_op2)
        self.btn_op2.pack()
        
    def mostrar_op2(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = SearchAlunoFrame(self,nomes)
        self.current_frame.pack(fill ="both", expand=True)

    def mostrar_op1(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = AddNotaFrame(self)
        self.current_frame.pack(fill ="both", expand=True)