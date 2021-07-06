import sqlite3

c = sqlite3.connect('base.db') #Connection
m = c.cursor() #mouse

def CreateTable():
    m.execute('create table if not exists data2 (Name TEXT,Surname,TEXT,Job TEXT,Age INT )')
    c.commit()

def AddData(NAME,SURNAME,AGE):
    m.execute("insert into data2 values (?,?,?)",(NAME,SURNAME,AGE))
    c.commit()
    
def CheckData():
    m.execute("Select * From data2")
    list = m.fetchall()
    for i in list:
        print(i)

def UpdateData(data):
    m.execute("Update veri2 set AGE = ? where AGE = 6",(data,))
    c.commit()

def RemoveData(data):
    m.execute("Delete From veri2 where NAME = ?",(data,))
    c.commit()

m.close

