import sqlite3

def create_db():
    con = sqlite3.connect('user.sqlite')
    cur = con.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        score INTEGER,
        status TEXT,
        name TEXT,
        pfdo INTEGER
    ); 
    '''
    cur.execute(query)
    con.commit()
    con.close()
def create_store():
    con = sqlite3.connect('store.sqlite')
    cur = con.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        article TEXT,
        about TEXT,
        type TEXT,
        price INTEGER
    ); 
    '''
    cur.execute(query)
    con.commit()
    con.close()
def insert_user(id, name_user, pfdo):
    con = sqlite3.connect('user.sqlite')
    cur = con.cursor()

    cur.execute(f'INSERT INTO users (user_id, score, status, name, pfdo) VALUES ({id}, 0,"user", "{name_user}", {pfdo});')
    con.commit()
    con.close()
def insert_product(name, type, price, about):
    con = sqlite3.connect('store.sqlite')
    cur = con.cursor()

    cur.execute(f'INSERT INTO products (article, about, type, price) VALUES ("{name}", "{about}", "{type}", {price});')
    con.commit()
    con.close()

def update_data(name, id, column, data):
    con = sqlite3.connect(f'{name}.sqlite')
    cur = con.cursor()
    sql_query = f"UPDATE users SET {column} = ? WHERE user_id = ?;"
    cur.execute(sql_query , (data, id,))
    con.commit()
    con.close()
def select_data(id):
    con = sqlite3.connect(f'user.sqlite')
    cur = con.cursor()
    data = cur.execute(f'''
    SELECT *
    FROM users
    WHERE user_id = {id}
    ''')
    data = data.fetchall()
    con.commit()
    con.close()
    return data
def datafr(name, table):
    con = sqlite3.connect(f'{name}.sqlite')
    cur = con.cursor()
    data = cur.execute(f'''
    SELECT *
    FROM {table}
    ''')
    data = data.fetchall()
    con.commit()
    con.close()
    return data
def user_database(id, name_user, pfdo):
    data = datafr("user")
    for i in range(len(data)):
        if data[i][1] == id:
            return True
    insert_user(id,name_user, pfdo)
    return False
def user_db(name, id):
    data = datafr(name, "users")
    for i in range(len(data)):
        if data[i][1] == id:
            return True
    return False
