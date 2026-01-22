import customtkinter as ctk
from py.backend import notas

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


class ListaOutput(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.linhas = []

    def adicionar_linha(self, texto):
        label = ctk.CTkLabel(self, text=texto, anchor="w")
        label.grid(row=len(self.linhas), column=0, sticky="ew", padx=5, pady=2)
        self.linhas.append(label)

    def limpar(self):
        for label in self.linhas:
            label.destroy()
        self.linhas.clear()

class Permateria(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(7, weight=1)

        # ---------- ALUNO ----------
        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome do aluno")
        self.entry_nome.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.entry_nome.bind("<KeyRelease>", self.on_keyrelease_nomes)

        self.optionmenu_nomes = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu_nomes.grid(row=1, column=0, sticky="ew", padx=5)
        self.optionmenu_nomes.set(" ")
        self.optionmenu_nomes.bind("<<CTkOptionMenuSelected>>", self.select_item_nomes)

        # ---------- SALA ----------
        self.entry_sala = ctk.CTkEntry(self, placeholder_text="Sala")
        self.entry_sala.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.entry_sala.bind("<KeyRelease>", self.on_keyrelease_salas)

        self.optionmenu_salas = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu_salas.grid(row=3, column=0, sticky="ew", padx=5)
        self.optionmenu_salas.set(" ")
        self.optionmenu_salas.bind("<<CTkOptionMenuSelected>>", self.select_item_salas)

        # ---------- MATÉRIA ----------
        self.entry_materia = ctk.CTkEntry(self, placeholder_text="Matéria")
        self.entry_materia.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        self.entry_materia.bind("<KeyRelease>", self.on_keyrelease_materias)

        self.optionmenu_materias = ctk.CTkOptionMenu(self, values=[])
        self.optionmenu_materias.grid(row=5, column=0, sticky="ew", padx=5)
        self.optionmenu_materias.set(" ")
        self.optionmenu_materias.bind("<<CTkOptionMenuSelected>>", self.select_item_materias)

        # ---------- BOTÃO ----------
        self.btn_buscar = ctk.CTkButton(self, text="Buscar média do aluno", command=self.buscar_media_materia)
        self.btn_buscar.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

        # ---------- RESULTADOS ----------
        self.lista_resultados = ListaOutput(self)
        self.lista_resultados.grid(row=7, column=0, sticky="nsew", padx=5, pady=5)

    # ---------------- BUSCAR MÉDIA ----------------

    def buscar_media_materia(self):
        nome = self.entry_nome.get().strip()
        sala = self.entry_sala.get().strip()
        materia = self.entry_materia.get().strip()

        self.lista_resultados.limpar()

        if not (nome and sala and materia):
            self.lista_resultados.adicionar_linha("Preencha Nome, Sala e Matéria.")
            return

        media = notas.geral_gradeb(nome, sala, materia)

        self.lista_resultados.adicionar_linha(
            f"Média de {materia} — {nome} ({sala}): {media:.2f}"
        )

    # ---------------- AUTOCOMPLETE ----------------

    def on_keyrelease_nomes(self, event):
        typed = self.entry_nome.get().lower()
        if not typed:
            self.optionmenu_nomes.configure(values=[])
            return

        filtered = [n for n in nomes if typed in n.lower()]
        self.optionmenu_nomes.configure(values=filtered)
        self.optionmenu_nomes.set(filtered[0] if filtered else " ")

    def on_keyrelease_salas(self, event):
        name_typed = self.entry_nome.get().strip().lower()
        typed_sala = self.entry_sala.get().strip().lower()

        nome_chave = None
        for nome in aluno_sala:
            if nome.lower().startswith(name_typed):
                nome_chave = nome
                break

        if not nome_chave:
            self.optionmenu_salas.configure(values=[])
            return

        filtered = [s for s in aluno_sala[nome_chave] if typed_sala in s.lower()]
        self.optionmenu_salas.configure(values=filtered)
        self.optionmenu_salas.set(filtered[0] if filtered else " ")

    def on_keyrelease_materias(self, event):
        typed = self.entry_materia.get().lower()
        if not typed:
            self.optionmenu_materias.configure(values=[])
            return

        filtered = [m for m in materias if typed in m.lower()]
        self.optionmenu_materias.configure(values=filtered)
        self.optionmenu_materias.set(filtered[0] if filtered else " ")

    # ---------------- SELEÇÕES ----------------

    def select_item_nomes(self, event):
        selected = self.optionmenu_nomes.get()
        if selected.strip():
            self.entry_nome.delete(0, "end")
            self.entry_nome.insert(0, selected)

    def select_item_salas(self, event):
        selected = self.optionmenu_salas.get()
        if selected.strip():
            self.entry_sala.delete(0, "end")
            self.entry_sala.insert(0, selected)

    def select_item_materias(self, event):
        selected = self.optionmenu_materias.get()
        if selected.strip():
            self.entry_materia.delete(0, "end")
            self.entry_materia.insert(0, selected)

class GeralGrade(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(5, weight=1)

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

        self.btn_buscar = ctk.CTkButton(self, text="Buscar média do aluno", command=self.buscar_media_geral)
        self.btn_buscar.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        self.lista_resultados = ListaOutput(self)
        self.lista_resultados.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

    # ---------------- BUSCAR MÉDIA ----------------

    def buscar_media_geral(self):
        nome = self.entry_nome.get().strip()
        sala = self.entry_sala.get().strip()

        self.lista_resultados.limpar()

        if not (nome and sala):
            self.lista_resultados.adicionar_linha("Preencha Nome e Sala.")
            return

        media = notas.geral_gradeb(nome, sala)

        self.lista_resultados.adicionar_linha(f"Média d {nome} ({sala}): {media:.2f}")

    # ---------------- AUTOCOMPLETE ----------------

    def on_keyrelease_nomes(self, event):
        typed = self.entry_nome.get().lower()
        if typed == "":
            self.optionmenu_nomes.configure(values=[])
            return

        filtered = [nome for nome in nomes if typed in nome.lower()]
        self.optionmenu_nomes.configure(values=filtered)
        self.optionmenu_nomes.set(filtered[0] if filtered else " ")

    def on_keyrelease_salas(self, event):
        name_typed = self.entry_nome.get().strip().lower()
        typed_sala = self.entry_sala.get().strip().lower()

        chave_nome = None
        for nome in aluno_sala:
            if nome.lower().startswith(name_typed):
                chave_nome = nome
                break

        if not chave_nome:
            self.optionmenu_salas.configure(values=[])
            return

        filtered = [s for s in aluno_sala[chave_nome] if typed_sala in s.lower()]
        self.optionmenu_salas.configure(values=filtered)
        self.optionmenu_salas.set(filtered[0] if filtered else " ")

    def select_item_nomes(self, event):
        selected = self.optionmenu_nomes.get()
        if selected.strip():
            self.entry_nome.delete(0, "end")
            self.entry_nome.insert(0, selected)

    def select_item_salas(self, event):
        selected = self.optionmenu_salas.get()
        if selected.strip():
            self.entry_sala.delete(0, "end")
            self.entry_sala.insert(0, selected)
