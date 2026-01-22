from py.gui.op1_add import AddNotaFrame
from py.gui.op2_search import SearchAlunoFrame
from py.backend import notas

import customtkinter as ctk

nomes, salas, materias, aluno_sala = notas.load_names()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monitoramento de Notas")
        geometry = "800x600"
        self.geometry(geometry)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        # Botões do menu principal
        self.btn_op1 = ctk.CTkButton(self, text="Adicionar Nota", command=self.mostrar_op1)
        self.btn_op1.grid(row=0, column=0,sticky="ew",padx=300, pady=5)

        self.btn_op2 = ctk.CTkButton(self, text="Pesquisar Aluno", command=self.mostrar_op2)
        self.btn_op2.grid(row=1, column=0,sticky="ew",padx=300, pady=5)


        
    def mostrar_op1(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = AddNotaFrame(self)
        self.current_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    def mostrar_op2(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = SearchAlunoFrame(self)
        self.current_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    def voltar_menu(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
            del self.current_frame
        # Aqui você poderia mostrar novamente os botões do menu, se eles tivessem sido escondidos
        print("Voltando ao menu principal...")