import tkinter as tk


root = tk.Tk()
root.title("Monitoramento de notas")

def add_to_list():
   text =  entry.get()
   if text:
        text_list.insert(tk.END, text)

frame = tk.Frame(root)
frame.grid(row = 0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry_bnt = tk.Button(frame, text="add")
entry_bnt.grid(row=0, column=0)

text_list = tk.Listbox(frame)
text_list.grid(row=1, column=0)

root.mainloop()