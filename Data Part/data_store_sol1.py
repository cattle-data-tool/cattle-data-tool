#provided csv files have 16 measurments per second


import sqlite3
import csv

class Data:
    db = sqlite3.connect(':memory:')
    def __init__(self):
        cursor = self.db.cursor()
        cursor.execute('''
         CREATE TABLE cows(cowId INTEGER,cowExtId INTEGER,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z)
            ''')
        self.db.commit() #commit to database
        
        print("Database in ram created")

    def add_csv(self, csvpath):
        cursor = self.db.cursor()
        with open(csvpath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count+= 1 #skip first line of CSV file, Column names are in there
                    
                else:          
            
                    tstp = row[15] 
                    tstp = tstp[14:19]   #remove date and hours from timestamp
                
                    line_count += 1
                    cursor.execute('''INSERT INTO cows(cowId,cowExtId,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(row[6],row[7],row[12],tstp,row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24]))
        
        
          
        self.db.commit()
        return("Done adding CSV")

    def getAcc(self,id,limb):
        cursor = self.db.cursor()
        cursor.execute("SELECT acc_x,acc_y  FROM cows WHERE (cowId = ? AND snsrPos = ? ) ",(id,limb,))
        all_rows = cursor.fetchall()
        step = 0
        dict = {}
        for row in all_rows: # row[0] returns the first column in the query 
        
            
            a = (step,row[0],row[1])
            dict[step] = a
            step += 1 
        

        return (dict)
    
    
        
            
            
a =  Data()
print(a.add_csv("DATA_01_05_Cow_42.csv")) #returns 42 and some other iDs

accs = a.getAcc(42,"RF")
for id in accs:
    print(accs[id])


"""
db = sqlite3.connect(':memory:') #make database in ram

cursor = db.cursor()#create new db cusor,can use it later 
cursor.execute('''
    CREATE TABLE cows(cowId INTEGER,cowExtId INTEGER,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z)
''')
db.commit() #commit to database


def getGyro(id,limb):
    cursor.execute("SELECT acc_x,acc_y  FROM cows WHERE (cowId = ? AND snsrPos = ? ) ",(id,limb,))
    all_rows = cursor.fetchall()
    step = 0
    dict = {}
    for row in all_rows: # row[0] returns the first column in the query 
    
        
        a = (step,row[0],row[1])
        dict[step] = a
        step += 1 
    

    print (dict[1])
            



def inputcsv(csvpath):
    cursor = db.cursor()
    with open(csvpath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count+= 1 #skip first line of CSV file, Column names are in there
                
            else:          
        
                tstp = row[15] 
                tstp = tstp[14:19]   #remove date and hours from timestamp
            
                line_count += 1
                cursor.execute('''INSERT INTO cows(cowId,cowExtId,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(row[6],row[7],row[12],tstp,row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24]))
                
        print(f'Processed {line_count} lines.')
    # db.commit()
        print("---------------------------------------------------------------")
        db.commit()
        
        cursor = db.cursor()


inputcsv("DATA_01_05_Cow_42.csv")
inputcsv("DATA_01_05_Cow_195.csv")
inputcsv("DATA_01_05_Cow_345.csv")
inputcsv("DATA_01_05_Cow_407.csv")
#getGyro(42)

getGyro(195,'RB')
"""