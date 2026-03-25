def get_user(id):
    return db.execute('SELECT * FROM users WHERE id = %s', (id,))