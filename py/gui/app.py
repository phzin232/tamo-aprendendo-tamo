from py.gui.op1_add import AddNotaFrame
from py.gui.op2_search import SearchAlunoFrame
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monitoramento de Notas")

        # Botões do menu principal
        self.btn_op1 = ctk.CTkButton(self, text="Adicionar Nota", command=self.mostrar_op1)
        self.btn_op1.pack()

        self.btn_op2 = ctk.CTkButton(self, text="Pesquisar Aluno", command=self.mostrar_op2)
        self.btn_op2.pack()

    def mostrar_op1(self):
        frame = AddNotaFrame(self)
        frame.pack()

    def mostrar_op2(self):
        frame = SearchAlunoFrame(self)
        frame.pack()
