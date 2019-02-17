import sqlite3

db = sqlite3.connect('my_first_db.db')
db.row_factory = sqlite3.Row
cur = db.cursor()

cur.execute('create table if not exists phones (brand text, version int)')

brand = input('Enter brand of phone')
version = int(input('Enter version of phone (as an integer)'))

cur.execute('insert into phones values (?, ?)', (brand, version))

for row in cur.execute('select * from phones'):
    print(row)


# cur.execute('drop table phones')

db.commit()

db.close()