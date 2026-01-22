import customtkinter as ctk
from py.backend import notas
from py.gui.op2_permateria import Permateria
from py.gui.opn2_geral import GeralGrade

nomes, salas, materias, aluno_sala = notas.load_names()


class SearchAlunoFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        self.btn_geral = ctk.CTkButton(self, text="Nota geral do aluno", command=self.show_geral_grade)
        self.btn_geral.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.btn_pesquisar = ctk.CTkButton(self, text="Nota por matéria", command=self.per_merteria)
        self.btn_pesquisar.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.btn_voltar = ctk.CTkButton(self, text="Voltar", command=parent.voltar_menu)
        self.btn_voltar.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    def per_merteria(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = Permateria(self)
        self.current_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    def show_geral_grade(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = GeralGrade(self)
        self.current_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)


