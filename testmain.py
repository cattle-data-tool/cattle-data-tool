from plotter import Plotter
from data import CsvDataBase

data = CsvDataBase()


plotter = Plotter(data)
"""
data.add_csv("DATA_01_05_Cow_42.csv")
data.add_csv(".xml files\DATA_01_05_Cow_195.csv")
data.add_csv(".xml files\DATA_01_05_Cow_345.csv")
data.add_csv(".xml files\DATA_01_05_Cow_407.csv")
data.add_csv(".xml files\DATA_01_05_Cow_407.csv")
data.add_csv(".xml files\DATA_02_02_Cow_608.csv")
"""
#print(data.addedFiles()) #print already added files
print(data.load_db("export.db")) #export database to file,returns list of tuples,just like add_csv()
#data.load_db("backup.db") #load database to ram,previous database will be destroyed,can call this function on load
#data.add_csv("DATA_01_05_Cow_42.csv") #will skip this file again,because it was saved to localdb,exported,loaded...and it is still in db
