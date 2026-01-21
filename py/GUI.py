import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def main():
    app = Application()
    app.mainloop()

class Application(ctk.CTk):
    def __init__(self, ):
        super().__init__()
        self.title("Monitoramento de notas")
        self.geometry("800x400")


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        frame = InputForm(self)
        frame.grid(row = 0, column=0, sticky="nsew",padx=5, pady=5)

        frame2 = InputForm(self)
        frame2.grid(row = 0, column=1, sticky="nsew",padx=5, pady=5)


class InputForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        

        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row=0, column=0,sticky="ew")

        self.entry.bind("<Return>", lambda event: self.add_to_list())

        self.entry_bnt = ctk.CTkButton(self, text="add",command=self.add_to_list)
        self.entry_bnt.grid(row=0, column=1)

        self.entry_bnt = ctk.CTkButton(self, text="Clear",command=self.clear_list)
        self.entry_bnt.grid(row=0, column=2)

        self.text_list = ctk.CTkTextbox(self, height=200)
        self.text_list.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.listbox = ctk.CTkTextbox(self, height=200)
        self.listbox.configure(state ="disabled")

    def add_to_list(self):
        text =  self.entry.get()
        if text:
            self.text_list.insert("end", text + "\n")
            self.listbox.configure(state ="normal") 
            self.listbox.configure(state ="disabled")
            self.entry.delete(0, "end")

    def clear_list(self):
        self.listbox.configure(state ="normal")  # Enable editing
        self.text_list.delete("1.0", "end")
        self.listbox.configure(state ="disabled")  # Disable editing


if __name__ == "__main__":
    main()