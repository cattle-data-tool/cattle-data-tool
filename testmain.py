from plotter import Plotter
from data import CsvDataBase

data = CsvDataBase()


plotter = Plotter(data)

print(data.add_csv("DATA_01_05_Cow_42.csv")) #will skip this file
exit()
data.remove_by_id(42)
data.add_csv("DATA_01_05_Cow_42.csv")
data.add_csv("DATA_01_05_Cow_42.csv")
data.remove_by_id(42)

#print(data.addedFiles()) #print already added files
data.export_db("backup1.db") #export database to file
#data.load_db("backup.db") #load database to ram,previous database will be destroyed,can call this function on load
#data.add_csv("DATA_01_05_Cow_42.csv") #will skip this file again,because it was saved to localdb,exported,loaded...and it is still in db
