from peewee import *


db = SqliteDatabase('cats.sqlite')


class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db


    def __str__(self):
        return f'{self.name} is a {self.color} cat and is {self.age} years old'


db.connect()
db.create_tables([Cat])

print('\nCreate and save 3 cats')

zoe = Cat(name="Zoe", color='Ginger', age=3)
zoe.save()

holly = Cat(name="Holly", color='Tabby', age=7)
holly.save()

mog = Cat(name="Mog", color='Black', age=1)
mog.save()

print('\nFind all cats')

cats = Cat.select()

for cat in cats:
    print(cat)