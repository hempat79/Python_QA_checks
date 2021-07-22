import sqlite3
from sqlite3 import Error

database = r"/home/patel60/qa_tests/QA Checks/Channel.db"

class utils:

    def __init__(self):
        self.database = database
        self.connection = None
        self.cursor = None

    def create_connection(self):
           
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            print("Error connecting to database!")    


    def run_create_insert_query(self, create_table_sql):
   
        try:
            self.cursor.execute(create_table_sql)
        except Error as e:
            print(e)



    def select_all_rows(self, sql):
        try:
            self.cursor.execute("SELECT code, test_sql FROM qa_tests where enabled = 'Y'")
            rows = self.cursor.fetchall()     
            #print(rows)            
            return rows

        except Error as e:
            print(e)    


    

    def close_connection(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        