import sqlite3

"""
Создать таблицу articles с полями:
id - идентификатор записи
title - заголовок
text - текст
created_at - дата создания

Написать функции для создания/редактирования/удаления/получения записей

При получении записей позволить пользователю искать по заголовоку или тексту
"""

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

cursor.execute('insert into users (email, password) values ("petr1@gmail.com", "qwerty123")')
connection.commit()

def create_table():
	query = '''
	    CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		email varchar(12) UNIQUE,
		password VARCHAR(30),
		name VARCHAR(40) DEFAULT "Noname"
	)
	'''
	cursor.execute(query)
	connection.commit()

create_table()

for i in range(5):
    email = input('Email: ')
    password = input('Password: ')
    name = input('Name: ')
    try:
 		cursor.execute(f'insert into users (email, password, name) values ("{email}", "{password}", "{name}")')
 		connection.commit()
    except sqlite3.IntegrityError:
            print('Email already exists')

