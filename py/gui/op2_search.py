import customtkinter as ctk
from py.backend import notas

nomes, salas, materias, aluno_sala = notas.load_names()

class SearchAlunoFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        self.btn_search = ctk.CTkButton(self, text="Nota geral do aluno", command=self.show_geral_grade)
        self.btn_search.grid(row=1,column=0,sticky="ew", padx=5, pady=5)


        self.btn_search = ctk.CTkButton(self, text="Pesquisar Aluno", command=self.pesquisar)
        self.btn_search.grid(row=2,column=0,sticky="ew", padx=5, pady=5)


        self.btn_voltar = ctk.CTkButton(self, text="Voltar", command=parent.voltar_menu)
        self.btn_voltar.grid(row=3,column=0,sticky="ew", padx=5, pady=5)

    def pesquisar(self):
        nome = self.entry_nome.get()
        sala = self.entry_sala.get()
        resultados = notas.search_student(nome)
        for resultado in resultados:
            print(resultado)

    def show_geral_grade(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = GeralGrade(self)
        self.current_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

# Frame scrollable para mostrar lista de resultados
class ListaOutput(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.linhas = []

    def adicionar_linha(self, texto):
        nome = self.entry_nome.get()
        sala = self.entry_sala.get()

        # if not(nome and sala):
        #     self.b


        label = ctk.CTkLabel(self, text=texto, anchor="w")
        label.grid(row=len(self.linhas), column=0, sticky="ew", padx=5, pady=2)

        
        self.linhas.append(label)

    def limpar(self):
        for label in self.linhas:
            label.destroy()
        self.linhas.clear()

class GeralGrade(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        # Entradas e botões
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome do aluno")
        self.entry_nome.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.entry_nome.bind("<KeyRelease>", self.on_keyrelease_nomes)

        self.optionmenu_nomes = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu_nomes.grid(row=1, column=0, sticky="ew", padx=5)
        self.optionmenu_nomes.set(" ")
        self.optionmenu_nomes.bind("<<CTkOptionMenuSelected>>", self.select_item_nomes)

        self.entry_sala = ctk.CTkEntry(self, placeholder_text="Sala")
        self.entry_sala.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.entry_sala.bind("<KeyRelease>", self.on_keyrelease_salas)

        self.optionmenu_salas = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu_salas.grid(row=3, column=0, sticky="ew", padx=5)
        self.optionmenu_salas.set(" ")
        self.optionmenu_salas.bind("<<CTkOptionMenuSelected>>", self.select_item_salas)

        self.bnt_buscar = ctk.CTkButton(self, text="Buscar Média Geral", command=self.buscar_media_geral)
        self.bnt_buscar.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        # Lista scrollable de resultados
        self.lista_resultados = ListaOutput(self)
        self.lista_resultados.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)


    def buscar_media_geral(self):
        nome = self.entry_nome.get().strip()
        sala = self.entry_sala.get().strip()

        if not (nome and sala):
            self.lista_resultados.limpar()
            self.lista_resultados.adicionar_linha("Por favor, preencha ambos os campos: Nome e Sala.")
            return

        total, quantidade, encontrado = notas.geral_gradeb(nome, sala)

        self.lista_resultados.limpar()

        if encontrado:
            media = total / quantidade if quantidade > 0 else 0
            self.lista_resultados.adicionar_linha(f"Média geral do aluno {nome} na sala {sala}: {media:.2f}")
        else:
            self.lista_resultados.adicionar_linha("Aluno não encontrado.")
    # Autocomplete nomes
    def on_keyrelease_nomes(self, event):
        typed = self.entry_nome.get().lower()
        if typed == "":
            self.optionmenu_nomes.configure(values=[])
            return

        filtered = [nome for nome in nomes if typed in nome.lower()]
        self.optionmenu_nomes.configure(values=filtered)
        if filtered:
            self.optionmenu_nomes.set(filtered[0])
        else:
            self.optionmenu_nomes.set(" ")

    # Autocomplete salas baseado no nome digitado
    def on_keyrelease_salas(self, event):
        name_typed = self.entry_nome.get().strip().lower()
        typed_sala = self.entry_sala.get().strip().lower()

        chave_nome = None
        for nome in aluno_sala.keys():
            if nome.lower().startswith(name_typed):
                chave_nome = nome
                break

        if not chave_nome:
            self.optionmenu_salas.configure(values=[])
            return

        filtered = [s for s in aluno_sala[chave_nome] if typed_sala in s.lower()]
        self.optionmenu_salas.configure(values=filtered)
        if filtered:
            self.optionmenu_salas.set(filtered[0])
        else:
            self.optionmenu_salas.set(" ")

    # Seleção de nome
    def select_item_nomes(self, event):
        selected = self.optionmenu_nomes.get()
        if selected.strip() != "":
            self.entry_nome.delete(0, "end")
            self.entry_nome.insert(0, selected)

    # Seleção de sala
    def select_item_salas(self, event):
        selected = self.optionmenu_salas.get()
        if selected.strip() != "":
            self.entry_sala.delete(0, "end")
            self.entry_sala.insert(0, selected)

