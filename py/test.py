import tkinter as tk
from tkinter import ttk

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self, ):
        super().__init__()
        self.title("Monitoramento de notas")


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        frame = InputForm(self)
        frame.grid(row = 0, column=0, sticky="nsew",padx=5, pady=5)

        frame2 = InputForm(self)
        frame2.grid(row = 0, column=1, sticky="nsew",padx=5, pady=5)


class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0,sticky="ew")

        self.entry.bind("<Return>", lambda event: self.add_to_list())

        self.entry_bnt = ttk.Button(self, text="add",command=self.add_to_list)
        self.entry_bnt.grid(row=0, column=1)

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def add_to_list(self):
        text =  self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)
            self.entry.delete(0, tk.END)


if __name__ == "__main__":
    main()