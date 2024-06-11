import sqlite3




def get_line(id: int) -> tuple:
        '''gets content from lines'''
        query = "select content from lines where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (id)).fetchone()
        return result
    
    
def create_line(content: str) -> int:
        '''inserts content into lines'''
        query = "insert into lines (content) values (?)"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (content,))
        return cursor.lastrowid
    
    
def delete_line(id: int):
        query = "delete from lines where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id))
                
    
def get_all_lines() -> list[tuple]:
        """select id, content from lines"""
        query = "select id, content from lines"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query).fetchall()
        return result