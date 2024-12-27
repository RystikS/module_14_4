import sqlite3

connection = sqlite3.connect('atari.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    initiate_db()


def insert_product(title, description, price):
    check_product = cursor.execute('SELECT * FROM Products WHERE title=?', (title,))

    if check_product.fetchone() is None:
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (title, description, price))
    connection.commit()


insert_product('Картина 1', 'Магазин "Lo-Fi"', 100)
insert_product('Картина 2', 'Девушка на стуле', 200)
insert_product('Картина 3', 'В ожидании официанта', 300)
insert_product('Картина 4', 'Loft-girl из Венгрии', 400)


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()
