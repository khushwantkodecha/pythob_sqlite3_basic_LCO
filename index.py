import sqlite3 ad lite

# functionalities come here
class DatabaseManage(objecet):
    def __init__(self):
        global con
        try:
            con = lite.connect('coursed.db')
            with con:
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,description TEXT,price TEXT,isPrivate BOOLEAN NOT NULL DEFAULT 1)')
        except Exception:
            print('unable to connect db!!!')
    # create data 
    def insert_data(self,data):
        try:
            with con:
                cur = con.cursor() 
                cur.execute("
                INSERT INTO course(name,description,price,isPrivate)
                VALUES (?,?,?,?)",data
                ")
        except Exception:
            return False
    # read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False
    # delete data
    def delete_data(self,id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql,[id])
        except expression as identifier:
            pass
        

#user interface comes here
