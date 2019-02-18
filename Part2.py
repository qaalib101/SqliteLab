import sqlite3
from peewee import *

db = SqliteDatabase('juggling_records2.db')

class Record(Model):
    record_holder = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db


    def __str__(self):
        return f'{self.record_holder} has {self.catches} catches and is from {self.country}'


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
    print('Thank you for using my program')


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
    db.create_tables([Record])
def add_fake_data():
    record1 = Record(record_holder="Ian Stewart", country="Canada", catches=94)
    record1.save()
    record2 = Record(record_holder="Aaron Gregg", country="Canada", catches=88)
    record2.save()
    record3 = Record(record_holder="Chad Taylor", country="USA", catches=78)
    record3.save()
def display_menu():
    print('--------------MENU-----------------')
    for item in menu:
        print('\n' + item)

def add_new_record():
    try:
        record_holder = input('Enter a new record holder name: ')
        country = input('Enter country of record holder: ')
        catches = int(input('Enter a number of catches'))
        record = Record(record_holder=record_holder, country=country, catches=catches)
        record.save()
        print('Adding was successful')
    except sqlite3.Error as e:
        print(e)
    except ValueError:
        print('Enter a correct integer')
def search_records():
    record_holder = input('Enter a record holder to find: ')
    try:
        records = []
        if record_holder == "":
            records = Record.select()
        else:
            records = Record.select().where(Record.record_holder==record_holder)
        if len(records) == 0:
            print("Nothin was found by the name: " + record_holder)
        else:
            for row in records:
                print(row)

    except sqlite3.Error as e:
        print(e)
def update_record():
    try:
        record_holder = input('Enter record holder to update: ')
        catches = int(input('Enter amount of catches'))
        query = (Record.update({Record.catches: catches}).where(Record.record_holder==record_holder))
        query.execute()
        print('\nrecord was successfully updated')
    except sqlite3.Error as e:
        print(e)
    except ValueError:
        print('You must enter the correct inputs')
def delete_record():
    record_holder = input('Enter the name of the record holder you wish to delete: ')
    try:
        query = Record.delete().where(Record.record_holder == record_holder)
        query.execute()
        print('\nrecord holder was successfully deleted')
    except sqlite3.Error as e:
        print(e)


main()