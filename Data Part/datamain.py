from data import Data

data = Data()

data.add_csv("DATA_01_05_Cow_407.csv") #import data from csv,can also specify location on computer,duplicate files rejected

print(data.getAccel(407))