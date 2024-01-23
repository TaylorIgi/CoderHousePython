
import functions_api
import functions_sql
import sqlite3

class MyDatabase:
    def __init__(self, db_name, db_conn):
        self.db_name = db_name
        self.db_conn = db_conn
        self.tables = []
    def add_table(self, new_table):
        self.tables.append(new_table)
    def list_tables(self):
        for table in self.tables:
            print(table)