from plotter_object import Plotter
plotter = Plotter()
from data import CsvDataBase
data = CsvDataBase()
data.add_csv(".xml files\DATA_01_05_Cow_407.csv")

accels_x = data.getAccel(407,'acc_x_g')
accels_y = data.getAccel(407,'acc_y_g')
cords = plotter.plotter_math(accels_x,accels_y)


cord_x = []
cord_y = []
for cord in cords:
    
 
    cord_x.append(cord[0])
    cord_y.append(cord[1])
    print(cord)


import matplotlib.pyplot as plt
x = cord_x
y = cord_y
plt.plot(x, y)
plt.show()