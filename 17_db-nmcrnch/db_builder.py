# KungFood - Johnny Wong, Sarar Aseer
# SoftDev1 pd8
# K16 -- No Trouble
# 2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#========================HELPER FXNS=======================
def tableCreator(tableName, col0, col1, col2):
    '''
    CREATES A 3 COLUMN TABLE
    ALL PARAMS ARE STRINGS
    '''
    command = "CREATE TABLE {0}({1}, {2}, {3});".format(tableName, col0, col1, col2)
    c.execute(command)

def insertInTable(file, tableName, columns):
    '''
    @columns should be a tuple of len 3 in order to access the row name in the csvfile
    The other params should be Strings
    '''
    command = "INSERT INTO {0}{1} VALUES(?, ?, ?)"
    with open(file, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = (row[columns[0]], row[columns[1]], row[columns[2]])
            c.execute(command.format(tableName, columns), data)

#==========================================================


#==========================================================
# INSERT YOUR POPULATE CODE IN THIS ZONE

# CREATE TABLE students TO HOLD peeps.csv INFO IN DB
tableCreator('students', 'name', 'age', 'id')

# OPEN peeps.csv AND TRANSFERS DATA TO TABLE peeps
insertInTable("peeps.csv", 'students', ('name', 'age', 'id'))

# CREATE TABLE courses TO HOLD courses.csv INFO IN DB
tableCreator('courses', 'code', 'mark', 'id')

# OPEN courses.csv AND TRANSFERS DATA TO TABLE courses
insertInTable("courses.csv", 'courses', ('code', 'mark', 'id'))
#==========================================================

db.commit() #save changes
db.close()  #close database
