import sqlite3


if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key,name varchar(20))')
    cursor.execute('insert into user(id,name) values (\'1\', \'Michael\')')
    print("create table user success!")
    cursor.close()
    conn.commit()
    conn.close()