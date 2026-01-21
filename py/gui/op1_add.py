import customtkinter as ctk
from py.backend import notas 

# Carrega nomes de alunos
nomes, salas, materias, aluno_sala = notas.load_names()

class AddNotaFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        # Nome com AutoComplete
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome do aluno")
        self.entry_nome.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.entry_nome.bind("<KeyRelease>", self.on_keyrelease_nomes)

        self.optionmenu = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu.grid(row=1, column=0, sticky="ew", padx=5)
        self.optionmenu.set(" ")  # vazio inicial
        self.optionmenu.bind("<<CTkOptionMenuSelected>>", self.select_item_nomes)

        # Sala AutoComplete
        self.entry_sala = ctk.CTkEntry(self, placeholder_text="Sala")
        self.entry_sala.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.entry_sala.bind("<KeyRelease>", self.on_keyrelease_salas)

        self.optionmenu3 = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu3.grid(row=3, column=0, sticky="ew", padx=5)
        self.optionmenu3.set(" ")  # vazio inicial
        self.optionmenu3.bind("<<CTkOptionMenuSelected>>", self.select_item_salas)

        # Matéria AutoComplete
        self.entry_materia = ctk.CTkEntry(self, placeholder_text="Matéria")
        self.entry_materia.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.entry_materia.bind("<KeyRelease>", self.on_keyrelease_materias)

        self.optionmenu2 = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu2.grid(row=5, column=0, sticky="ew", padx=5)
        self.optionmenu2.set(" ")  # vazio inicial
        self.optionmenu2.bind("<<CTkOptionMenuSelected>>", self.select_item_materias)

        #Entry para atividade e nota
        self.entry_atividade = ctk.CTkEntry(self, placeholder_text="Atividade")
        self.entry_atividade.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

        self.entry_nota = ctk.CTkEntry(self, placeholder_text="Nota")
        self.entry_nota.grid(row=7, column=0, sticky="ew", padx=5, pady=5)

        # Botão para salvar
        self.btn_add = ctk.CTkButton(self, text="Adicionar Nota", command=self.add_grade)
        self.btn_add.grid(row=8, column=0, pady=10)

    # Atualiza sugestões nessa ordem, Nome sala e materia
    def on_keyrelease_nomes(self, event):
        typed = self.entry_nome.get().lower()
        if typed == "":
            self.optionmenu.configure(values=[])
            return

        filtered = [nome for nome in nomes if typed in nome.lower()]
        self.optionmenu.configure(values=filtered)
        if filtered:
            self.optionmenu.set(filtered[0])
        else:
            self.optionmenu.set(" ")

    def on_keyrelease_salas(self, event):
        name_typed = self.entry_nome.get().strip().lower()
        typed_sala = self.entry_sala.get().strip().lower()

        nome_chave = None

        for nome in aluno_sala.keys():
            if nome.lower().startswith(name_typed):
                nome_chave = nome
                break

        if not nome_chave:
            self.optionmenu3.configure(values=[])
            return

        filtered = [s for s in aluno_sala[nome_chave] if typed_sala in s.lower()]
        self.optionmenu3.configure(values=filtered)

        if filtered:
            self.optionmenu3.set(filtered[0])
        else:
            self.optionmenu3.set(" ")

    def on_keyrelease_materias(self, event):
        typed = self.entry_materia.get().lower()
        if typed == "":
            self.optionmenu2.configure(values=[])
            return

        filtered = [materia for materia in materias if typed in materia.lower()]
        self.optionmenu2.configure(values=filtered)
        if filtered:
            self.optionmenu2.set(filtered[0])
        else:
            self.optionmenu2.set(" ")

    # Seleciona do OptionMenu
    def select_item_nomes(self, event):
        selected = self.optionmenu.get()
        if selected.strip() != "":
            self.entry_nome.delete(0, "end")
            self.entry_nome.insert(0, selected)

    def select_item_salas(self, event):
        selected = self.optionmenu3.get()
        if selected.strip() != "":
            self.entry_nome.delete(0, "end")
            self.entry_nome.insert(0, selected)

    def select_item_materias(self, event):
        selected = self.optionmenu2.get()
        if selected.strip() != "":
            self.entry_materia.delete(0, "end")
            self.entry_materia.insert(0, selected)

    # Salva a nota no backend
    def add_grade(self):
        nome = self.entry_nome.get()
        sala = self.entry_sala.get()
        materia = self.entry_materia.get()
        atividade = self.entry_atividade.get()
        nota = self.entry_nota.get()

        if not (nome and sala and materia and atividade and nota):
            self.btn_add.configure(text="Preencha todos os campos!")
            return

        try:
            nota_float = float(nota)
        except ValueError:
            self.btn_add.configure(text="Nota inválida!")
            return

        sucesso = notas.add_grade(nome, sala, materia, atividade, nota_float)
        if sucesso:
                    self.btn_add.configure(text="Nota Adicionada!")
        else:
            self.btn_add.configure(text="Erro ao adicionar nota!")


        # Limpa campos
        self.entry_nome.delete(0, "end")
        self.entry_sala.delete(0, "end")
        self.entry_materia.delete(0, "end")
        self.entry_atividade.delete(0, "end")
        self.entry_nota.delete(0, "end")
        self.optionmenu.set(" ")
