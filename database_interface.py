import sqlite3




def get_line(id: int) -> tuple:
        '''gets content from lines'''
        query = "select content from lines where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (id,)).fetchone()
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




def get_fullCommit(id: int) -> tuple:
        '''gets name, directory, fileCommitIdsJson from fullCommits'''
        query = "select name, directory, fileCommitIdsJson from fullCommits where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (id)).fetchone()
        return result

def get_fullCommit_by_name(name: str) -> tuple:
        '''gets name, directory, fileCommitIdsJson from fullCommits'''
        query = "select name, directory, fileCommitIdsJson from fullCommits where name = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, (name,)).fetchone()
        return result
    
    
def create_fullCommit(name, directory, fileCommitIdsJson) -> int:
        '''inserts name, directory, fileCommitIdsJson into fullCommits'''
        print(f"inside create_fullCommit: {name}, {directory}, {fileCommitIdsJson}")
        query = "insert into fullCommits (name, directory, fileCommitIdsJson) values (?, ?, ?)"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (name, directory, fileCommitIdsJson))
        return cursor.lastrowid
    
    
def update_fullCommit(name, directory, fileCommitIdsJson, id: int) -> int:
        '''updates name, directory, fileCommitIdsJson in fullCommits table'''
        query = "update fullCommits set name = ?, directory = ?, fileCommitIdsJson = ? where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, name, directory, fileCommitIdsJson, id)
    
    
def delete_fullCommit(id: int):
        query = "delete from fullCommits where id = ?"
        with sqlite3.connect('main.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, (id))
                
    
