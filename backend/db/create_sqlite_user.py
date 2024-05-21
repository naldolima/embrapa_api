import sqlite3
from datetime import datetime

def add_user(conn, user):
    sql = ''' INSERT INTO user(email,password,is_admin,is_active)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid



def main():
    try:
        with sqlite3.connect('embrapa.db') as conn:
            user = ('user@teste.com', '$2b$12$nhKyKQuC2jOiqwf4vKqaQuyUKtx3avyrpaM2N.QILTgUNTz3kWHJO',True, True)
            user_id = add_user(conn, user)
            print('Created user admin success')


    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    main()