import sqlite3
def get_user(username):
    db = sqlite3.connect('users.db')
    
    query = "SELECT * FROM users WHERE username = '%s'" % username
    return db.execute(query)
