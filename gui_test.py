from gui import Gui
from plotter import Plotter
from data import CsvDataBase

data = CsvDataBase()
plotter = Plotter()

app = Gui(data, plotter)
app.mainloop()
