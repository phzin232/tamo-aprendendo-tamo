from py.backend import notas
from py.gui import app as gui

app = gui.App()
notas.load_names()

app.mainloop()
