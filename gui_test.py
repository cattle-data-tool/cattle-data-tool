from gui import Gui
from plotter import Plotter
from data import CsvDataBase

data = CsvDataBase()
plotter = Plotter(data)

app = Gui(data, plotter)
app.geometry("1280x720")
app.mainloop()
