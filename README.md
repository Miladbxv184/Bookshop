# DIS project: Bookshop

##### by Milad Maidan bxv184.

## E/R-diagram
![bookshop.png](/bookshop.png)

## Technical setup
### Virtual environment
Create and activate a virtual environment.

    python -m venv venv
    venv\Scripts\activate

### Requirements
Run the code below to install the necessary modules.

    pip install -r requirements.txt

### Set up the database
Initialize the database by running the `import_csv.py` script, which will create the necessary tables and import the data.

    python app/models.py

### Run the application

    python run.py

### How to use
I have generated an example user.

    username: username
    password: password

You can also register your own user.

## Description of fulfillment of requirements
### SQL queries
The `routes.py` file includes several examples of interacting with the database using SQL:

#### INSERT
Used in user registration and placing orders.

    conn.execute('INSERT INTO USERS (username, password) VALUES (?, ?)', (username, password))
    conn.execute('INSERT INTO orders (order_date, total_price, username) VALUES (?, ?, ?)', (order_date, total_price, username))


#### UPDATE
Used in changing passwords.

    conn.execute('UPDATE USERS SET password = ? WHERE username = ?', (new_password, session['username']))


#### DELETE
Used in deleting orders.

    conn.execute('DELETE FROM order_items')
    conn.execute('DELETE FROM orders')


#### SELECT
Used in various routes to fetch data from the database.

    user = conn.execute('SELECT * FROM USERS WHERE username = ? AND password = ?', (username, password)).fetchone()
    books = conn.execute('SELECT id, title FROM books').fetchall()


#### RegEx
The search functionality in `routes.py` uses regular expressions to match book titles.





