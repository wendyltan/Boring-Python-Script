import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("drop table user")
    cursor.close()
    print("Delete table success!")
    conn.commit()
    conn.close()