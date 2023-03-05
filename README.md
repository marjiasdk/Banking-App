# Python Banking App

This is a simple banking app created with Python and the Tkinter GUI toolkit. The app allows users to log in with their name, card number and password and view their account balance.

# Technologies

* Python: a powerful and versatile programming language that is used widely in a variety of fields, from web development to data analysis.
* Tkinter: a standard GUI toolkit for Python that allows developers to create desktop applications with a user interface.
* MYSQL: a popular open-source relational database management system that provides fast and scalable storage for large amounts of data.
* mysql-connector-python mpdule: a Python library that allows Python programs to access MySQL databases using the Python Database API specification.

# Getting Started

To run the app, you will need to have Python and the Tkinter module installed on your system. You will also need to have a MySQL database set up with a "users" table containing the user's name, card number, password, and account balance.

To set up the database, you can use the following SQL script:
```
CREATE DATABASE banking;

USE banking;

CREATE TABLE users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  card_number VARCHAR(16),
  password VARCHAR(255),
  balance DECIMAL(10, 2)
);

INSERT INTO users (name, card_number, password, balance) VALUES
('John Smith', '1234567890123', 'password123', 1000.00),
('Jane Doe', '2345678901234', 'password456', 500.00),
('Bob Johnson', '3456789012345', 'password789', 250.00),
('Sarah Lee', '4567890123456', 'passwordabc', 100.00),
('David Kim', '5678 901234567', 'passworddef', 50.00);
```
Be sure to update the database connection details in the banking_app.py file to match your own MySQL server settings.
<br></br>
<i> I have omitted the password from my own code for privacy reasons, simply replace the empty space with the password to your MYSQL connection. </i>

# Usage

To run the app, run the ```banking_app.py``` file in your Python environment. The app will open a window with fields for entering a name, the card number and password.

If the entered name, card number and password match a record in the database, the user's account balance will be displayed. If the details do not match, an error message will be displayed.

# License

This project is licensed under the MIT License. You are free to use, modify, and distribute this code for personal or commercial purposes. However, the original author(s) must be credited and this license statement must be included in all copies of the code.
