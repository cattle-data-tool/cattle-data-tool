from plotter import Plotter
plotter = Plotter()
from data import CsvDataBase
data = CsvDataBase()
data.add_csv("DATA_01_05_Cow_42.csv") #load file to  database in ram,also returns key indentifiers such as iD,internaliD,externaliD
data.add_csv("DATA_01_05_Cow_42.csv") #will skip this file
print(data.addedFiles()) #print already added files
data.export_db("backup.db") #export database to file
data.load_db("backup.db") #load database to ram,previous database will be destroyed,can call this function on load
data.add_csv("DATA_01_05_Cow_42.csv") #will skip this file again,because it was saved to localdb,exported,loaded...and it is still in db

accels_x = data.getAccel(42,'acc_x_g')
accels_y = data.getAccel(42,'acc_y_g')
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