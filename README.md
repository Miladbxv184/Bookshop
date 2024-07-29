# DIS project: Bookshop

##### by Milad Maidan bxv184.

## ER-diagram
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
We have generated an example user.

    username: username
    password: password

You can also register your own user.

## Description of fulfillment of requirements
### SQL queries
The `routes.py` file includes several examples of interacting with the database using SQL:

#### INSERT
Inserting user data during registration:

  ```python
  conn.execute('INSERT INTO USERS (username, password) VALUES (?, ?)', (username, password))
  conn.execute('INSERT INTO orders (order_date, total_price, username) VALUES (?, ?, ?)', (order_date, total_price, username))


- Inserting book data when a user adds a book:
  ```python
  sql = text("INSERT INTO book (title, author, pages, user_id) VALUES (:title, :author, :pages, :user_id)")
  db.session.execute(sql, {'title': form.title.data, 'author': form.author.data, 'pages': form.pages.data, 'user_id': current_user.id})
  db.session.commit()


#### UPDATE
We use the `UPDATE` statement to update user or book details.

- For example, updating the read_pages of a book could look like:
  ```python
  sql = text("UPDATE book SET read_pages = :read_pages WHERE id = :book_id")
  db.session.execute(sql, {'read_pages': new_read_pages, 'book_id': book_id})
  db.session.commit()

#### DELETE

We use `DELETE` statements to remove data. 
- For example, deleting a book:
  ```python
  sql = text("DELETE FROM book WHERE id = :book_id")
  db.session.execute(sql, {'book_id': id})
  db.session.commit()

#### SELECT
We use multiple `SELECT` statements in our code to fetch data.
- For example, fetching books for a user's dashboard:
  ```python
  sql = text("SELECT * FROM book WHERE user_id = :user_id")
  books = db.session.execute(sql, {'user_id': current_user.id}).fetchall()

#### RegEx
We use regular expressions in our application for input validation and data processing:
- Email Validation:
  ```python
  def is_valid_email(email):
      regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
      return re.match(regex, email) is not None





