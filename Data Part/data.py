#provided csv files have 16 measurments per second

import sqlite3
import csv
import os #not sure if this works on Linux,ask Petar to check!

class Data:
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    added_files = "" #list of added files
    def __init__(self):
        
        self.cursor.execute('''
         CREATE TABLE cows(dataId INTEGER PRIMARY KEY AUTOINCREMENT,cowId INTEGER,cowExtId INTEGER,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z)
            ''')
        self.db.commit() #commit to database
        
        print("Database in ram created")

    def add_csv(self, csvpath):
        if str(csvpath) not in self.added_files:
            with open(csvpath) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count+= 1 #skip first line of CSV file, Column names are in there
                    elif line_count == 1:
                        tstp = row[15] 
                        tstp = tstp[14:19]
                        self.cursor.execute('''INSERT INTO cows(cowId,cowExtId,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(row[6],row[7],row[12],tstp,row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24]))
                        indentifier = (row[6],row[7],row[9])
                        line_count += 1
                        
                    else:          
                
                        tstp = row[15] 
                        tstp = tstp[14:19]   #remove date and hours from timestamp
                    
                        line_count += 1
                        self.cursor.execute('''INSERT INTO cows(cowId,cowExtId,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(row[6],row[7],row[12],tstp,row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24]))
            
            
            
            self.db.commit()
            self.added_files += str(csvpath)
            return(indentifier)
        else:
            print("This file is already added")
            return(-1)

    def export_db(self,filename):
    
        def exportit():
            db_backup = sqlite3.connect(filename)
            newCursor = db_backup.cursor()
            newCursor.execute('''
                CREATE TABLE cows(cowId INTEGER,cowExtId INTEGER,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z)
                ''')
            db_backup.commit() #commit to database
                
            self.cursor.execute("SELECT * FROM cows")
            all_rows = self.cursor.fetchall()
            for row in all_rows:
                newCursor.execute('''INSERT INTO cows(cowId,cowExtId,snsrPos,timeStamp,acc_x,acc_x_g,acc_y,acc_y_g,acc_z,acc_z_g,gyro_x,gyro_y,gyro_z) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''',(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
            db_backup.commit()
            print("Data Saved Sucessfully")
            return(1)



        if os.path.isfile(filename):
            try:
                os.remove(filename)
                exportit()
                
            except: 
                #not sure to kill the code here or just return(error) or return (-1)
                raise RuntimeError("You need to close file " ,filename, " before atempting to save to it!")
                #return ("Close the file,idiot!")
        else:
            exportit()
 
    def getAccel(self,id,column = "acc_x_g"):
        limb = "RF"
        #limb = "LF"
        #lib = "Ear"
        #column = "acc_x_g"
        #column = "acc_y_g"
        #column = "acc_x"
        #column = "acc_y"
        self.cursor.execute("SELECT acc_x_g  FROM cows WHERE (cowId = ? AND snsrPos = ? ) ",(id,limb,))
        all_rows = self.cursor.fetchall()
        step = 0
        dict = {}
        for row in all_rows: # row[0] returns the first column in the query 
              
            a = (step,row[0])
            dict[step] = a
            step += 1 
        

        return (dict)
