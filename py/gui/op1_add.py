from py.backend import notas
import customtkinter as ctk





class AddNotaFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome do Aluno")
        self.entry_nome.pack()

        self.entry_sala = ctk.CTkEntry(self,placeholder_text="Sala do Aluno")
        self.entry_sala.pack()

        self.entry_materia = ctk.CTkEntry(self, placeholder_text="Matéria")
        self.entry_materia.pack()

        self.entry_atividade = ctk.CTkEntry(self, placeholder_text="Atividade")
        self.entry_atividade.pack()

        self.entry_nota = ctk.CTkEntry(self, placeholder_text="Nota")
        self.entry_nota.pack()  

        self.btn_add = ctk.CTkButton(self, text="Adicionar Nota", command=self.adicionar)
        self.btn_add.pack()

    def adicionar(self):
        nome = self.entry_nome.get()
        sala = self.entry_sala.get()
        materia = self.entry_materia.get()
        atividade = self.entry_atividade.get()
        nota = float(self.entry_nota.get())

        notas.add_grade(nome, sala, materia, atividade, nota)
        if notas.add_grade(nome, sala, materia, atividade, nota):
            self.btn_add.configure(text="Nota Adicionada com Sucesso!")
            
