import sqlite3

db = sqlite3.connect('juggling_records.db')
db.row_factory = sqlite3.Row
cur = db.cursor()

menu = ["1 Add a new record holder",
        "2 Search for a record holder",
        "3 Update an existing record holder",
        "4 Delete a record holder",
        "0 Quit"]
def main():
    choice = 1
    create_table()
    add_fake_data()
    while choice is not 0:
        display_menu()
        choice = int(input('Enter a menu choice'))
        while choice < 0 or choice > 4:
            print('\nEnter a correct number')
            choice = int(input('Enter a menu choice'))
        get_menu_option(choice)



def get_menu_option(choice):
    if choice == 1:
        add_new_record()
    elif choice == 2:
        search_records()
    elif choice == 3:
        update_record()
    elif choice == 4:
        delete_record()
def create_table():
    cur.execute('create table if not exists records (record_holder text, country text, catches int)')
def add_fake_data():
    cur.execute('insert into records values ("Ian Stewart", "Canada", 94)')
    cur.execute('insert into records values ("Aaron Gregg", "Canada", 88)')
    cur.execute('insert into records values ("Chad Taylor", "USA", 78)')
def display_menu():
    print('--------------MENU-----------------')
    for item in menu:
        print('\n' + item)

def add_new_record():
    record_holder = input('Enter a new record holder name: ')
    country = input('Enter country of record holder: ')
    catches = int(input('Enter a number of catches'))
    try:
        cur.execute('insert into records values(?, ?, ?)', (record_holder, country, catches))
    except sqlite3.Error as e:
        print(e)
def search_records():
    record_holder = input('Enter a record holder to find: ')
    try:
        if record_holder == "":
            query = 'select * from records'
            for row in cur.execute(query):
                print('record holder: ' + row['record_holder'])
                print('country: ' + row['country'])
                print('catches: ' + str(row['catches']))
        else:
            for row in cur.execute('select * from records where record_holder = ?', (record_holder,)):
                print(row['record_holder'])
                print(row['country'])
                print(row['catches'])
    except sqlite3.Error as e:
        print(e)
def update_record():
    try:
        record_holder = input('Enter record holder to update: ')
        catches = int(input('Enter amount of catches'))
        cur.execute('update records set catches = ? where record_holder = ?', (catches, record_holder))
        print('\nrecord updated')
    except sqlite3.Error as e:
        print(e)
    except ValueError:
        print('You must enter the correct inputs')
def delete_record():
    record_holder = input('Enter the name of the record holder you wish to delete: ')
    try:
        cur.execute('delete from records where record_holder = ?', (record_holder,))
        print('\nrecord holder was deleted')
    except sqlite3.Error as e:
        print(e)


main()

db.commit()
db.close()