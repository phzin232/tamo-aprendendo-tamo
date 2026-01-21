from py.gui.op1_add import AddNotaFrame
from py.gui.op2_search import SearchAlunoFrame
from py.backend import notas

import customtkinter as ctk

nomes = notas.load_names()

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

    def on_keyrelease(self,event):
        text = self.entry_nome.get()
        self.listbox_delete(0, ctk.END)
        for nome in nomes:
            if text.lower() in nome.lower():
                self.listbox_insert(ctk.END, nome)

    def select_iten(self,event):
        if not self.listbox.curselection():
            return
        selected = self.listbox.get(self.listbox.curselection())
        self.entry_nome.delete(0, ctk.END)
        self.entry_nome.insert(0, selected)
        
    def mostrar_op2(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = SearchAlunoFrame(self)
        self.current_frame.pack(fill ="both", expand=True)

    def mostrar_op1(self):
        if hasattr(self, 'current_frame'):
            self.current_frame.destroy()
        self.current_frame = AddNotaFrame(self)
        self.current_frame.pack(fill ="both", expand=True)