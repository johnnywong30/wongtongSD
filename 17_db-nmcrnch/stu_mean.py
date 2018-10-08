# Team DTong - Johnny Wong, Derek Song
# SoftDev1 pd8
# K17 -- Average
# 2018-10-05

import sqlite3   # enable control of an sqlite database
import csv       # facilitates CSV I/O

# set up to read/write to db file

DB_FILE="discobandit.db"
db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#========================HELPER FXNS=======================
def tableCreator(tableName, col0, col1):
    '''
    CREATES A 2 COLUMN TABLE
    ALL PARAMS ARE STRINGS
    '''
    command = "CREATE TABLE {0}({1}, {2});".format(tableName, col0, col1)
    c.execute(command)

def insertInTable(tableName, data):
    '''
    @tableName is the name the table being written to
    @data is the dictionary of data used
    '''
    command = "INSERT INTO {0} VALUES(?, ?)"
    for key, value in data.items():
        info = (key, value)
        c.execute(command.format(tableName), info)

def insertRow(tableName, data):
    '''
    @tableName is the name the table being written to
    @data is the dictionary of data used
    '''
    command = "INSERT INTO {0} VALUES(?, ?, ?)"
    c.execute(command.format(tableName), data)

def computeAverages(table1, table2, columns):
    '''
    @columns should be a tuple of len 3 to access columns of tables wanted
    The other params should be Strings
    Looks up name, students.id, mark from students and courses tables
    '''

    # inner helper fxn to find the avg
    def avg(a, b, c):
        sum = int(a) + int(b)
        return sum / c

    command = 'SELECT {0}, {1}, {2} FROM {3}, {4} WHERE {1} = {4}.id'
    c.execute(command.format(columns[0], columns[1], columns[2], table1, table2))
    rows = c.fetchall()
    dict_of_avgs = {}
    id_count = 0 # num of courses the id has
    for row in rows:
        # if the id is in the dict
        if row[1] in dict_of_avgs:
            # course count increments
            id_count += 1
            # new average is calculated and assigned to that id key
            # calculation done by ((currentAvg * currentNumOfCourses) + newGrade ) / currentNumOfCourses + 1
            dict_of_avgs[row[1]] = avg(dict_of_avgs[row[1]] * (id_count - 1) , row[2], id_count)
        else:
            # course count for that id starts at 1
            id_count = 1
            # that id's average is their first course grade
            dict_of_avgs[row[1]] = row[2]
    return dict_of_avgs

def insertAverages(data):
    # insert averages from input dictionary of key:val pairs of ('id':average)
    insertInTable('peeps_avg', data)


def displayAverages(table1, table2, columns):
    # prints out averages of each person
    # does not update when courses are added currently
    command = 'SELECT {0}, {3}.{1}, {2} FROM {3}, {4} WHERE {3}.{1} = {4}.{1}'
    cur = c.execute(command.format(columns[0], columns[1], columns[2], table1, table2))
    rows = cur.fetchall()
    print('NAME | ID | AVERAGE')
    dispRow = '{0} | {1} | {2}'
    for row in rows:
        print(dispRow.format(row[0], row[1], row[2]))

def addCourse(code, mark, id):
    # adds course to the course table in DB_FILE from input column data
    insertRow('courses', (code, mark, id))
#==========================================================
# creates peeps_avg table in DB_FILE
# tableCreator('peeps_avg', 'id', 'average' )

# dictionary of key:val pairs of ('id':average)
averages = computeAverages('students', 'courses', ('name', 'students.id', 'mark'))

# insert ids and corresponding avgs to peeps_avg
#insertAverages(averages)

# displays averages in format NAME | ID | AVERAGE
displayAverages('students', 'peeps_avg', ('name', 'id', 'average'))

# adds course macroeconomics with mark of 65 and id of 3
#addCourse('macroeconomics', '65', '3')

#==========================================================
db.commit() #save changes
db.close()  #close database
