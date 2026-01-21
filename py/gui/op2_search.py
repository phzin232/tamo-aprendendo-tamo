from py.backend import notas
import customtkinter as ctk



class SearchAlunoFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome do Aluno")
        self.entry_nome.pack()

        self.entry_sala = ctk.CTkEntry(self, placeholder_text="Sala do Aluno")
        self.entry_sala.pack()

        self.btn_search = ctk.CTkButton(self, text="Pesquisar Aluno", command=self.pesquisar)
        self.btn_search.pack()

    def pesquisar(self):
        nome = self.entry_nome.get()
        sala = self.entry_sala.get()
        resultados = notas.search_student(nome)
        for resultado in resultados:
            print(resultado)