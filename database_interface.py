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


def get_lines_in(listOfIds: list[int]) -> list[tuple]:
    query = "select id, content from lines where id in ({seq})".format(seq=','.join('?'*len(listOfIds)))
    with sqlite3.connect('main.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, listOfIds).fetchall()
    return result




def get_fileCommit(id: int) -> tuple:
        '''gets name, commitSigJson, fileName from fileCommits'''
        query = "select name, commitSigJson, fileName from fileCommits where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (id,)).fetchone()
        return result
    
    
def create_fileCommit(name, commitSigJson, fileName) -> int:
        '''inserts name, commitSigJson, fileName into fileCommits'''
        query = "insert into fileCommits (name, commitSigJson, fileName) values (?, ?, ?)"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (name, commitSigJson, fileName))
        return cursor.lastrowid
    
    
def update_fileCommit(name, commitSigJson, fileName, id: int) -> int:
        '''updates name, commitSigJson, fileName in fileCommits table'''
        query = "update fileCommits set name = ?, commitSigJson = ?, fileName = ? where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, name, commitSigJson, fileName, id)
    
    
def delete_fileCommit(id: int):
        query = "delete from fileCommits where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id))
                
    
def get_all_fileCommits() -> list[tuple]:
        """select id, name, commitSigJson, fileName from fileCommits"""
        query = "select id, name, commitSigJson, fileName from fileCommits"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query).fetchall()
        return result

def getCommitByName(commitName: str) -> tuple:
    query = "select id, name, commitSigJson, fileName from fileCommits where name = ?"
    with sqlite3.connect('main.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, (commitName,)).fetchone()
    return result