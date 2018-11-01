from data_store_sol1 import Data

data = Data()


 
data.add_csv("DATA_01_05_Cow_42.csv") 

data.add_csv("DATA_01_05_Cow_42.csv") #import data from csv,can also specify location on computer

data.export_db("data.sqlite") #filename.db or filename.sqlite,can also specify location on compter,

