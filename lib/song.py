from config import CONN, CURSOR
import sqlite3

class Song:
    
    def __init__(self,name,album):
        self.name=name
        self.album=album
        
    @classmethod
    def create_table(self):
        sql = """
         CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
    #CURSOR.execute(sql)
# CONN = sqlite3.connect('sqlite3/music.db')
# CURSOR = CONN.cursor()