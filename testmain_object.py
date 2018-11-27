
from plotter_object import Plotter
plotter = Plotter()
from data import CsvDataBase
data = CsvDataBase()
data.add_csv("DATA_01_05_Cow_42.csv")

accels_x = data.getAccel(42,'acc_x_g')
accels_y = data.getAccel(42,'acc_y_g')
print(plotter.plotter_math(accels_x,accels_y))
