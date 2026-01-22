import customtkinter as ctk
from py.backend import notas

nomes, salas, materias, aluno_sala = notas.load_names()

class AutocompleteEntry(ctk.CTkEntry):
    def __init__(self, parent, placeholder_text="", values=None, *args, **kwargs):
        super().__init__(parent, placeholder_text=placeholder_text, *args, **kwargs)
        self.values = values if values is not None else []
        self.optionmenu = ctk.CTkOptionMenu(parent, values=[])
        self.optionmenu.set(" ")
        self.optionmenu.grid(row=self.grid_info()["row"] + 1, column=self.grid_info()["column"], sticky="ew", padx=5)
        self.bind("<KeyRelease>", self.on_keyrelease)
        self.optionmenu.bind("<<CTkOptionMenuSelected>>", self.select_item)

    def on_keyrelease(self, event):
        typed = self.get().lower()
        if typed == "":
            self.optionmenu.configure(values=[])
            return

        filtered = [value for value in self.values if typed in value.lower()]
        self.optionmenu.configure(values=filtered)

    def select_item(self, event):
        selected = self.optionmenu.get()
        self.delete(0, ctk.END)
        self.insert(0, selected)
        self.optionmenu.configure(values=[])


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
