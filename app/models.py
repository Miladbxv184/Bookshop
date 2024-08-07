import sqlite3

def get_db_connection():
    conn = sqlite3.connect('booksclean.db')
    return conn

def create_table_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        authors TEXT,
        description TEXT,
        category TEXT,
        publisher TEXT,
        price REAL,
        publish_month TEXT,
        publish_year INTEGER
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def create_table_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def create_table_orders():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        total_price REAL,
        order_date TEXT,
        FOREIGN KEY (username) REFERENCES users(username)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def create_table_order_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        order_id INTEGER,
        book_id INTEGER,
        PRIMARY KEY (order_id, book_id),
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
    """)
    conn.commit()
    cur.close()
    conn.close()

def import_csv_data():
    import csv
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        with open('BooksDatasetClean.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                title, authors, description, category, publisher, price, publish_month, publish_year = row
                cur.execute(
                    "INSERT INTO books (title, authors, description, category, publisher, price, publish_month, publish_year) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (title, authors, description, category, publisher, float(price), publish_month, int(publish_year))
                )
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error occurred during data import: {str(e)}")
    finally:
        cur.close()
        conn.close()

def add_default_user():
    conn = get_db_connection()
    conn.execute('DELETE FROM users')  # Clear existing users for this example
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('username', 'password'))
    conn.commit()
    conn.close()

def clean_author_names():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE books SET authors = REPLACE(authors, 'By ', '') WHERE authors LIKE 'By %'")
    conn.commit()
    cur.close()
    conn.close()

def init_db():
    create_table_books()
    create_table_users()
    create_table_orders()
    create_table_order_items()
    import_csv_data()
    clean_author_names()
    add_default_user()

if __name__ == '__main__':
    init_db()
